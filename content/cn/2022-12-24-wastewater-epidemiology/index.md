---
title: 生活废水新冠病毒浓度监测流程
author: Miao Yu
date: '2022-12-24'
slug: wastewater-epidemiology
tags:
  - covid
---

最近国内疫情进展非常快，我处于三四线城市的家人在这周陆续都阳性了，远超卫健委报的那个数。然而，我们却并没有能准确获知疫情进展的途径，当前利用搜索引擎、微博调查及身边统计学搞出的那些玩意太容易被主观情绪污染而且也仅覆盖了互联网用户。同时，中国当前的老年人其实更多分布在乡村，他们当前可能还没受到冲击，但春运开始后，可以预见会出现不小的医疗资源缺口，但没有数据做指导可能互联网的舆论关注不到。作为科研人员，我更希望看到实实在在的客观指标。

我的专业背景是环境化学，在过去的三年期间，我看到了很多利用城市污水处理厂进行流行病学研究的报道。城市污水处理厂是城市水溶性污染物的一个汇，其数值波动可以有效反应城市尺度上污染状况的波动而城市污水厂的水样监测其实也是各地环保监测站的日常工作。如果我们能够利用监测数据给出新冠病毒的浓度变化趋势，那么也就大致掌握了当地的疫情进展。同时，因为新冠的感染与发病通常存在一个时间差，环境样品中病毒载量达峰也能很好预测未来一到两周的临床确诊，这对于有限医疗资源的调用非常重要。

废水流行病学对于防疫决策的作用在过去两年已经被很多国家所接纳。美国biobot公司与美国疾控中心合作，日常公布其对美国县级水平的废水中新冠病毒监测[数据](https://biobot.io/data/)。从其数据中我们可以得知，去年年底omicron在美国的大流行时，废水中新冠病毒浓度要提早临床发病人数大概一到两周。目前该公司则将工作重心放在了监测废水中阿片类药物上。在[欧洲](https://ec.europa.eu/environment/water/water-urbanwaste/info/pdf/Waste%20Waters%20and%20Covid%2019%20MEMO.pdf)，荷兰水中发现新冠病毒要早于其第一例新冠病例三周，西班牙早了一个月而意大利米兰则早了快两个月，欧盟多国也启动了类似[监测](https://www.eureau.org/resources/news/529-monitoring-covid-19-in-waste-water)计划。根据欧盟估算，对单一污水处理厂进行新冠病毒的每日监测的一年总花销约为25000欧元，如果改为一周两测（目前能拿到可靠数据的最低要求），对应花销更低。其实国内已经有很多课题组进行了相关研究，但目前还没有出现监测级别的数据。

其实，搭建一个从样品采集到数据展示的全流程生活废水新冠病毒浓度监测项目并不困难。这里我将参考2020年发表在*nature*上的一篇[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8325066/)给出一个可实操的流程。

## 样品采集与分析

采集污水厂初沉池污泥40mL（固体含量2.6%-5%，分析前-80°C保存），取2.5mL污泥用商用土壤总RNA提取试剂盒（RNeasey PowerSoil Total RNA Kit, Qiagen）提取样品中总RNA。提取RNA后取RNA组分溶解在50uL无核酸纯净水里，用分光光度计测定总RNA含量。

然后，使用美国疾控中心推荐的一步法 RT-RCR 来定量样品中的新冠病毒，方法文件网上[有](https://www.fda.gov/media/134922/download?fbclid=IwAR1DdEweazD3ixmrpZMc07VXM0_n1qx455rGV7E0fAEcA1QZf3Peh0Qxypo)。这里的原理是用N1与N2引物片段或探针测定新冠病毒含量，这个引物网上有[卖](https://www.idtdna.com/pages/landing/coronavirus-research-reagents/cdc-assays)的，不到200美元，而且序列是已知的，WHO给出了相关[信息](https://www.who.int/docs/default-source/coronaviruse/whoinhouseassays.pdf)也可以自己合成。这里同时要加上人源的RP基因，只有样品里含有RP基因才认为测到了新冠病毒。这里具体定量要根据你的仪器来，论文里使用了Bio-Rad iTaq Universal Probes One-Step Kit 这个试剂盒，条件为

> 20-µl reactions run at 50°C for 10 min and 90°C for 1 min, followed by 40 cycles of 95°C for 10s and 60°C for 30s per the manufacturer’s recommendations

SARS-CoV-2的RNA浓度要用标准曲线矫正。具体方法就是要合成SARS-CoV-2RNA的DNA作为模版，然后用其扩增N基因，之后用MEGAscript T7 Kit来产生单链RNA，这个RNA拷贝数已知（记录扩增过程参数），用前述RT-PCR荧光光度计定量响应，逐级稀释后生成标准曲线。这样就可以知道样品中病毒浓度。不过，我们要用第一步总RNA含量来进行矫正。这个方法在5倍稀释条件下未发现qRT–PCR的抑制作用。

同时，作为质量控制，请使用2018年污泥样品作为阴性对照。

这个样品处理流程并不需要P4实验室，污泥中的病毒RNA被提取后也没什么活性，一个常规生物实验室应该就可以做到日常测定。我能想到的唯一问题就是污泥可能非常臭，不过这对环境化学的科研人员而言应该已经习惯了。

## 数据分析

当你已经有了样品中病毒浓度，可以用散点图加趋势线的方法来快速生成病毒浓度趋势。

不过，其实当前如果你能同时做到测序，就可以同时给出不同变种的变化趋势，这里可以直接用UCSD给出的数据处理[镜像](https://github.com/ucsd-ccbb/C-VIEW)与今年发表在*nature*上的[论文](https://pubmed.ncbi.nlm.nih.gov/35798029/)。

其实这个实验操作没有任何技术难点，用到的全都是商用试剂盒与成熟的仪器，对于研究型实验室当材料准备好应该一天内就能做出来，对于监测站可能要写个更详细的标准操作流程，但最多一周也可以用了。我们读论文并不是为了发文章，而是让其真正产生社会价值，眼下这个周期已经被各种自动化仪器与标准试剂盒大大缩短了。

希望有条件实验室尽快构建实验室标准操作流程开始监测，可以通过社交网络公布所在城市与区域的病毒载量达峰状况，这样可能会给易感人群争取到1-2周的缓冲期来调配资源。对于污水的采样可以不局限于城市污水厂，乡村生活污水也可以进行监测。

长远看国内需要在现有全国尺度的环境监测站上部署相关设备，及时对公共卫生事件进行预警，估计每年都会有几次。