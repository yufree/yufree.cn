---
title: 《穹顶之下》影响力测算
date: 2015-03-07
slug: chai influence
tags:
  - popsci
  - data
---

同多数环境相关专业同学一样，这一周我的微博微信被《穹顶之下》相关讨论轮番轰炸，不论褒贬大家都有一个共识：那就是这部纪录片确实产生了很大的影响力，所以才有必要去争论。我也很好奇，究竟一部纪录片而不是制作它的人或团队会产生什么样的影响？到底大不大？存不存在偏见？因此我做了一点探索分析，这部分分析完全基于网络开放工具，也因此每个接触互联网的人都可以重现我的结果，至于结论，各花入各眼。

## 思路

全文中提取高频词汇作为关键词，然后对关键词的搜索趋势进行分析作为《穹》的影响力测算依据，分析尺度有三：这7天来趋势的变化；搜索地域差异；搜索人群特征。也就是说从时间，空间与参与者三个角度评价《穹》的影响，起码符合记叙文三要素。我本打算用谷歌趋势，结果搜索量太低形不成趋势，因此转而使用[百度指数](http://index.baidu.com/)，虽然结果可重复，但存在一些缺点我们文末再议。

## 报告文本

其实第二天我们就可以从网络上搜索得到《穹》的[全文](http://vdisk.weibo.com/s/tEXDd1OHvRYy)，利用在线[词云制作工具](http://timdream.org/wordcloud/)，在去除掉一些无意义的高频词后得到如下词云：

![](https://yufree.github.io/blogcn/figure/wordcloud.png)

很佩服，全文高频词里没有特别专业的词汇，但又确实在讨论一个专业问题。本来我想通过高频词搜索的一些性质来进行下一步检索，现在看不行。

## 关键词选择

因为我也完整看了一遍视频，所以列选了一些关键词，首先看穹顶与12369这两个词：

![](https://yufree.github.io/blogcn/figure/keywords1.png)

《穹》播出后12369的搜索热度要强于纪录片本身，这说明人们确实对内容而不仅仅是片子本身产生了兴趣，而且后续的媒体指数也跟进了，因此我选了更多视频中出现的关键词而不是视频本身或制作人本身作为下一步探索影响力的基础。

## 时间趋势

见下图：

![](https://yufree.github.io/blogcn/figure/keywords2.png)
![](https://yufree.github.io/blogcn/figure/keywords3.png)
![](https://yufree.github.io/blogcn/figure/keywords4.png)

我选择的关键词为褐煤、空气净化器、pm10、环保部与12369。你要问我为什么不多选点，那是百度太抠门，最多选5个（谷歌也有限制）。现象如下：

- 7天过去，搜索强度没有回归到基线，影响力仍在
- 12369，褐煤的搜索高峰要早于空气净化器与环保部
- 移动端上述现象不明显
- 移动端的影响力上升下降的峰比PC端更陡峭

针对第一条，我很想知道究竟一个新闻事件造成的影响能用多久回归到基线，据此对比最近另一个热词duang的搜索趋势：

![](https://yufree.github.io/blogcn/figure/duang.png)

在duang面前，12369已经恢复到了基线…为此我又尝试了另外几组词，最后在尝试马航时，我发现两者强度相对接近：

![](https://yufree.github.io/blogcn/figure/mh.png)

去年年底的马航惨剧互联网用了11天左右恢复到基线，类比12369，估计这次关于纪录片的讨论可能持续半个月左右。很强了，现在的信息更迭速度可以用秒来记，能抓住人们半个月的注意力很不容易。有人批中国喜欢搞运动，但有比没有强啊，三分钟热度也是热度，有热度就效果。

后面几条的现象会在人群特征中重新提及。

## 空间趋势

刚才是全国的搜索趋势，具体到城市会不会有差异？去年虽然全年空气质量达标的城市不多，但总还是有，污染较重的也有，为此我选取济南，唐山，拉萨，三亚作为检测城市，结果如下：

![](https://yufree.github.io/blogcn/figure/sp.png)
![](https://yufree.github.io/blogcn/figure/sppc.png)
![](https://yufree.github.io/blogcn/figure/spmo.png)

整体上，污染城市比非污染城市对视频关键词的搜索指数高（当然我也不清楚百度究竟用了什么算法，很可能是人口基数造成的），甚至非污染城市已经回到了基线，但有意思的是在搜索上移动端的行为地域差异性小于PC端，另外一个有意思的地方是污染城市在视频播出前对12369就产生了搜索波动，我估计是跟当天污染状况有关。

据此，地域上影响力是有差异的，视频对污染城市的人影响似乎更大些。

## 人群特征

这里只使用了3月份数据来隔离之前搜索的影响（百度不提供精确到天的人群特征搜索查询），还是前面5个关键词：

![](https://yufree.github.io/blogcn/figure/age.png)

看起来似乎中年人比青年人更关注环保部而中老年人更关注空气净化器，而空气净化器这个词的性别比中女性要高于男性。但上面这个现象可能是假象，原因在于我们不知道基线在哪里？合不合理。你去看这个年龄分布会发现存在歧视：年龄很小与很大的网民可能不会去使用互联网，同时性别比也太离谱，基于此我增加了两个基线关键词，一个是新闻，我认为这个词各个年龄段的人都会关注，另一个是exo，虽然我不清楚这跟XO还有EX有啥区别，但风闻搜索这个词的女性要远高于男性，结果如下：

![](https://yufree.github.io/blogcn/figure/control.png)

额，就当我假设的基线正确吧，我们可以看到，中年人确实要比基线搜索更多的环保部，而中老年人则更喜欢搜索空气净化器，年轻人似乎对12369抱有更大的期望。至于性别，其实刚才的说法是站不住脚的，因为基线里女性比例要高于所有视频相关关键词，也就是说，关注视频的男性要比基线多，只是在空气净化器这个词上，男性关注相对小。另外根据exo这个词反映的性别比，我感觉百度给出的参数似乎有点偏误。

## 小结

### 时间尺度

- 大致持续10～15天回归基线
- PC端比移动端滞后，变化相对缓慢

### 空间尺度

- 污染重的城市比轻的城市关注度高，基线回归慢
- PC端趋势比移动端差异明显

### 人群

- 网络人群活跃度本身存在基线差异，做对比要设定基线与假设
- 青年人更响应视频号召去打电话
- 中年人比青年人更关注环保部，重行动
- 中老年人更关注空气净化器，重健康
- 女性比男性关注空气净化器，但低于新闻基线

## 吐槽

- 上面的结论一定有你觉得不合理的，数据就在那里，请自行探索事实
- 百度的趋势搜索功能限制太多，希望开放数据API，这样可以用google的[因果推断包](https://github.com/google/CausalImpact)来进行更有统计意义的时序推断，当然我知道这不太可能
- 关于影响力，上面所做的其实是基于互联网搜索数据的，存在偏误，所以不要得出太广泛的结论，讲段子除外
- 现在在线工具可以回答你很多问题，所以不要总是盯着自己生活圈内那一点点资讯，你的社交网络圈在同化你的同时也异化了你，跳出来看一下试试
- 互联网是一个娱乐致死的最佳样本