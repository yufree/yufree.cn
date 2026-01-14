---
title: 最小大语言模型
author: Miao Yu
date: '2026-01-14'
slug: sllm
categories: []
tags:
  - tech
---

我很早就在折腾本地大语言模型了，但平时主要还是用网页版或API调用，一方面是本地资源贫瘠，16GB内存供养不了大模型；另一方面，本地能跑的模型效果实在是有限。这两方面说的其实是一回事，那就是相比计算集群，我自己这点可用推理算力实在够呛，属于边缘计算了。但反观我们科研数据分析，到今天用得最多的还是线性回归跟假设检验，可见我的要求可能本来就是矫情。

跟着大语言模型成长这几年，从参数量越来越大，到数据不够了用合成数据，再到MoE构架激活少量参数，明显感觉一个旗舰模型大概在用的时候能激活20B到30B的参数已经非常优秀了，而低一个数量级也差不多够日常用了。但MoE构架的模型大都是稀疏的，我这电脑连本体都放不下，只能跑跑为端侧设计的 gemma3n 这种稠密模型。然而，就算是这种够日常用的，上下文也小的可怜。

然后我就开始想对策了。既然本地内存不够用，我可以租算力，也不贵。然而，我又有点担心数据泄露，查来查去，看中了远程过程调用(RPC)这个方案。简单说就是我用某个模型时在本地计算前几层，后面的计算扔到云端，这样就算被截胡，反推也比较难。我用colab尝试了下，确实可行，但由于当前超高的网络延迟也非常慢，这里记录下。

在Colab或服务器端，需要下载本地同样的模型与 llama.cpp ，要用ngrok来穿透内网，要开启缓存，不然更慢，如果你是在局域网服务器部署就更简单些，不需要ngrok做内网穿透，直接用内网IP：

```
# 1. 编译支持 RPC 的 llama.cpp
!git clone https://github.com/ggerganov/llama.cpp
%cd llama.cpp
!cmake -B build -DLLAMA_CUDA=ON -DGGML_RPC=ON
!cmake --build build --config Release -j$(nproc)

# 2. 安装并配置 ngrok (请替换为你的 Token)
!curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
!echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
!sudo apt update && sudo apt install ngrok
!ngrok config add-authtoken "YOUR_TOKEN"

# 3. 下载 MoE 模型
!pip install huggingface_hub
from huggingface_hub import hf_hub_download
model_path = hf_hub_download(repo_id="Qwen/Qwen2.5-1.5B-Instruct-GGUF", filename="qwen2.5-1.5b-instruct-q4_k_m.gguf")

# 4. 启动 RPC 服务
import subprocess
import os
import threading
import time
!pip install pyngrok
from pyngrok import ngrok

def run_rpc():
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = f"{os.getcwd()}/build/bin:" + env.get("LD_LIBRARY_PATH", "")
    
    try:
        process = subprocess.Popen(
            ['/content/llama.cpp/build/bin/rpc-server', '-H', '0.0.0.0', '-p', '50052','-c',  
        '--model-path', '/content/llama.cpp/models'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            cwd='/content/llama.cpp'
        )
        # 实时打印服务端日志，这样报错能立刻看到
        for line in process.stdout:
            print(f"[RPC Server] {line}", end='')
    except Exception as e:
        print(f"❌ 启动失败: {e}")

# 启动线程
threading.Thread(target=run_rpc, daemon=True).start()

# 等待服务端初始化 GPU 驱动
time.sleep(5) 

ngrok.kill() 
tunn = ngrok.connect(50052, "tcp")

print(f"\n" + "="*40)
print(f"🚀 RPC 服务端已就绪！")
print(f"🔗 本地 Mac 连接地址: {tunn.public_url.replace('tcp://', '')}")
print(f"="*40)
```

然后本机也要安装同样版本的 llama.cpp 跟模型，本地编译要加 `-DGGML_RPC=ON` 来保证包含RPC功能，默认的没有，然后设定本机只跑几层就可以，同时要打开 flash-attn 跟 no-mmap 来提高点效率：

```
./llama-cli -m ../../models/qwen2.5-1.5b-instruct-q4_k_m.gguf \
  --rpc NGROK_LINK \
  --n-gpu-layers 10 \
  --flash-attn on \
  --no-mmap \
  -p "你好"
```

效果不是很理想，只是能跑通，主要是传输过程的网络延迟，如果是局域网，把模型挂nas上应该没啥问题。但实话说这个方案比较鸡肋，双端都要加载部分模型，唯一优势就是本机上下文会大，速度快一点，局域网里如果计算节点够强其实也可以都在服务器端算，另一不明显优势就是可以防局域网内部信息泄漏。

我还尝试了另一个方案，就是准备两个模型，一个放在服务器上，另一个在本地跑，后者非常轻量，会快速响应用户，但生成的内容会分批次先通过网络送到服务器让服务器端大模型来审核，如果可以就直接放行，如果不行就打回去重新生成，这个技术是分布式投机采样（Distributed Speculative Decoding）。用小模型来投机，大模型来把关，网络延迟会被一次性审核抵消一部分，用户体感上会感觉快。我同样在本机跑了0.6B跟4B模型，其实反而更慢，主要是本机跑内存里要放两个模型，字数一多就容易爆内存。不过网络环境应该可以，但这里有个问题就是两个对接模型得有相似词表，也就是最好都是一个体系下不同参数量的模型。我了解了这个原理后，感觉openai的mini版还有gemini的flash版应该用了类似技术来加速，他们应该就是为旗舰模型训练了不少个小参数量的模型，搞不好就是放出来那些开源的，然后把旗舰模型放后端审核，这样会显著加快速度。这个方案并不会节省token，但会提速，应对不复杂的任务或日常任务应该够了，但要是复杂任务反而会因为打回重写比率比较高而不如直接服务器响应。家用或个人用场景里这个方案应该会是主流。

这应该也就是现在端侧模型的发展趋势，搭配一个端侧小模型来对用户需求评级。分为三档，第一档应对非常简单的指令小模型直接出答案，第二档常规任务端侧主力模型生成回复，必要时云端审核，第三档有难度需要思考的直接送云端做。这就体现出小模型的重要性了，我们并不需要他懂很多知识，只要能评判任务难度跟隐私保护，超纲的往云端送就可以了。而我们关注的个人隐私问题一般难度并不大，要么本地处理，要么本地脱敏。

这么来看，这大语言模型发展倒是跟医疗里分级诊疗有相似性。现在很多人感冒发烧也挂三甲专家号，本质是消耗了高端医疗资源，与之对应的是二甲或社区医院资源闲置，这里面缺的不是私人家庭医生制度，而是个体根本没有分级判断的能力。其实完全可以引入小语言模型来做分级预判，这个并不是诊断，只是预分流，没必要稍微不舒服就跑大医院或进急诊，这样也会有利于提高医疗资源利用率。而且现在AI对电力要求非常离谱，但我推测八成的需求根本用不上旗舰模型，所以很多商用产品才会出flash或fast版本，要是我的话对外就一个版本，然后配一个动态需求定价，省的用户搞鄙视链。

我看了很多人对大语言模型的自我感觉式评价，很多其实问题就没问好，没有开发好工具潜力，反过来又说模型不行。在当前的时间点，主流大语言模型知识储备都超过了平均社会人，你最好去问你水平在平均线下的问题，要是问平均线上的自然需要好些模型，以当代人的无知程度，大语言模型还是很有用的，就连那个0.6B的小模型做中英互译也比大多 how are you 型选手强了。平均社会人就跟平均工资一样也是偏态分布，在所有维度上都达到平均水平的人可以算超人了，大多数人属于平均中位数下面那一档，只是自我感觉良好罢了，我就是这类。

另外，解决软件工程问题的思路或许可以用在其他方面，毕竟从工资吸引力上看，目前做人工智能的人大概都是很聪明的人，他们的技术外溢对其他学科发展应该也会有启发。
