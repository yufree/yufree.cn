---
title: 噪音
author: Miao Yu
date: '2022-03-19'
slug: noise
categories: []
tags:
  - writing
---

最近在地铁上读完了《噪音》，这名义上是丹尼尔·卡尼曼的新书，不过读完我大概可以判断出来这是为了蹭《思考，快与慢》的热度。书商最重要的营销手段就是书的腰封，如果是新人作者一般都会找些名人推荐，但如果作者本身就很有名，那肯定会把作者其他成名作也放上去，怎么说丹尼尔·卡尼曼也是诺奖得主。而且估计下一本书一出，书商肯定又要说三部曲啥的，倒霉的赫拉利出的第三本书就被国内书商给翻译成了《今日简史》硬凑简史三部曲，而这本书的英文名其实是 *21 Lessons for the 21st Century*，出版社名字一改反而把原书的数字梗给扔掉了。

《噪音》这本书照例没跑出成名作即巅峰的规律，相当于从《思考，快与慢》里截出一部分扩展成一本书，甚至很多案例都没换。不过，我十分怀疑丹尼尔·卡尼曼究竟承担了多少写作内容，这本书的拼凑感非常强，很多地方跟《思考，快与慢》有衔接，但其他一些内容感觉像是为了凑噪音理论放上去的。不过，这本书的很多观点属于懂得都懂，但不懂得看了只会迷糊，我估计做过分析测量工作的人看了可能会很有体会。

本书一个核心观点是将人的判断错误分成了偏差与噪音两部分，偏差那部分就是《思考，快与慢》里提到的认知偏误，而噪音则有很多种。与之可以类比就是测量里信度与效度的概念，偏差的问题在于效度，也就是是否准确，认知偏误会导致效度降低，而噪音主要影响的是信度，也就是是否可信。或者更简单可以理解为均值与方差，认知偏误会导致均值不准而噪音大则表示数据方差大。噪音是明摆着不能消除的，但知道有噪音就很不容易了，现代人过于迷信当前的量化手段但不考虑量化的不确定性，或者说现代人过于依赖确定性带来的稳定感，这如同认知偏误一样会带来决策上的结果失误，而且很多时候其实不管你怎么决策都不能达到效果或者说影响最终结果。

然后，作者又进一步把噪音分解成了水平噪音、模式噪音与情景噪音。这段我读着就想笑，因为这显然是在重新定义噪音，如果噪音里有场景或模式及个人差异，其实就算不上噪音了。这里其实更多是想说清楚噪音的来源，不过其实绕来绕去说得就是线性混合模型的几个变种。水平噪音是个体异质性，例如同一案件两个法官量刑本来就有不同；模式噪音则是稳定的观点异质性，例如同一个法官就是喜欢重判有犯罪记录的人而轻判初犯；情景噪声则是不稳定的异质性，例如前面那个法官刚吃了饭心情不错，那么很有可能就轻判。放到线性混合模型里就是要同时考虑样本间斜率与截距都存在随机效应，而对随机效应建模是为了更好估计固定效应。不过，这段论述其实放到《思考，快与慢》里解释一些认知偏误也不会违和，从整体上看的噪音其实就有可能是个体认知偏误产生的。这里作者重新定义噪音其实很牵强，还不如直接解释下线性混合模型说得更清楚。

真正有点意思的是作者对噪音产生的讨论。在对法官自由裁量权的讨论里，我们天性会认为自由裁量权会带来因地制宜的审判，但同样会导致相同场景的两个人会被判出差别极大的结果。这里面多少是因为事件独特性不好衡量，但单纯看法官偏好或心情似乎就能解释其中相当一部分决策差异，理想与现实间总是隔着人性。另外，决策噪声容易被忽略的一个原因在于很多决策对于个体而言都是一锤子买卖，在无法观察平行宇宙的当下，单纯看结果可能归因错了，也可能压根就没有原因单纯是随机过程在起作用。人们评价决策会倾向于用决策的反面来推理，但总是忘了一件基本事实：你的决策可能本来对结果就不产生影响。你可能以为躲开一个小坑就能最后获胜，但更可能进到另一个大坑套小坑，坑里还有水，水里还有钉，钉上还有毒的场景。学会理解世界的不确定性是个体成熟的表现，也许你还是无可奈何，但不至于三观崩塌。当然，如果你能重复决策，那么肯定能从反馈里收益，只是这种机会目前还不是人人都有的。很多场景下的有效解决方案可能不易察觉，例如书里面就提到了白大褂综合症，一个病人去看病血压指标总是高，怎么吃药都不好，后来换了个医生，医生让他自己买一个血压计测就正常了，这里导致血压高的原因其实是病人自己一进诊所就紧张，知道这事后他去诊所反而不紧张了。不过并不是每个人都能换医生，很多人所陷入的困境自己出不来别人也无从下手去帮忙，有的时候是需要些外部刺激的。

这本书还提到了测量问题，认为均方误可以一定程度降低噪音。我觉得这个看法很重要，关键点不在均方误而在测量。我时常在想为啥跟纯理科背景的人交流起来如此困难，通常我会说是他们没有实际工作经验，但这个所谓实际工作经验又很模糊，不过测量确实可以作为一个精确描述。很多没实际做过测量的拿到的都是别人测好的数据，这些数据都是精确的数值，这样会极大程度方便数学建模。不过，如果不知道这些数据是怎么产生的，那么通常就不会对数据产生更深的认识。打比方很多污染物测量数据是在检出限附近测到的，所谓检出限就是仪器刚好能分辨真实信号与噪音的测量水平，此处的不确定度就会远高于10倍或20倍信噪比的测量值。但如果数据分析人员不知道，就可能从噪音里“看到”规律，毫无疑问这种规律没有任何价值，只是单纯技术水平的解析力达不到造成的。不过，现在很多人过于依赖数据库而忽略数据的产生过程，就会导致其发现没实际意义，这点有点类似type M型错误。如同书里所言：

> 我们不需要一个比我们测量更精确的模型

本书比较推崇简单模型，越简单越可操作越好。在作者看来，懂得越多，噪音越大。机械的判断，甚至是等权重判断都要比所谓的专家直觉判断来的靠谱。当然，这又是《思考，快与慢》里内容的复读，不过也确实值得复读。很多事因为存在太多未知变量，过于精细的模型确实反而不如简单线性回归来的稳健，很多人自作聪明去微调，但效果可能适得其反。我们总是听了太多大神大师的传奇故事，但传奇之所以传奇就是因为不常见，而我们生活的日常里也许机械判断就够了。现在很多人总是担心落伍，不断去学习新闻、新概念、新技术，但相比知识焦虑，更严重的可能是思考匮乏。很多人学知识只是为了跟风不落后或增加谈资，但知识如果不用学了也会忘，而考虑是否对自己有用或有意义正是独立思考的第一步。

本书另一个亮点在于对噪音如何放大的讨论。这里噪音的放大核心问题其实是个体判断的独立性被破坏，群体决策里如果出现带风向或意见极化的问题。其实这个很常见，如果算法总是推荐给你小布尔乔亚的精致生活，你自然会对自己产生额外的同群效应进而会焦虑不安。如果你看过《十二怒汉》，就会发现陪审团里如果不能达成内部统一，讨论会越来越激烈，固执己见是可能获胜的，但固执己见是否代表真相就是另一个问题了。我们日常见到的讨论经常是被少数人带风向的，大多有投票权的人既不了解讨论内容，也懒得独立思考，这样的后果就是少数服从多数只有形式上的民主而实际上则可能变成了少数人可操纵的独裁。群体一旦失去个体独立性，那么也很容易失去多样性，最后就都成了体制的零件，嘎吱嘎吱制造噪音。

本书另一重点是论述因果思维与统计思维的区别。这点其实跟我写的两种因果差不多，人们口口声声说要讲因果逻辑，但很多时候就是强行因果而不考虑概率与不确定性。很多人看了几本书，听了几次课就以为自己构建了一套解释万物的世界观，这当然要比没有世界观要好，但也好不到有优越感的地步，因为世界观往往是个人局限性的来源。很多人的观点都属于何不食肉糜或东宫娘娘烙大饼这个档次的，沉浸在自己的圈子与因果逻辑里会把世界也扭曲成自己的“合理”，但世界运行根本不在乎你怎么看。我记得2020年初，当时武汉刚封城，某个群里就有搞计算化学的人说自己算了下新冠病毒与受体结合过程，发现比SARS弱，应该问题不大，后面一堆人跟风崇拜。但事实上他用错了受体，这个计算被后来的大流行卷进了历史的垃圾堆。

人们太渴望确定性与掌控感了，但这恰恰是最难获取的。最近老家封城，我妈打电话抱怨说怎么就两年多都对付不了一个病毒？我听到后更多的感觉是不解，因为人类本来也没能对付几个病毒，黑死病那时间纯粹靠人死光了才渡过疫情的。而且我们即便到今天对这个病毒的了解也很不够，能做到一年出疫苗，两年实现几十亿人疫苗注射已经是很了不起了，即使疫苗对阻断传播效果有限，起码也降低了病死率。这个病毒与其变种不断打脸各类专家政客，这些其实才是最正常的，反而是03年非典莫名其妙的消失属于某种奇迹。确定性与掌控感是目标而不是结果，结果是啥样谁也不知道，要允许犯错而不是动不动就审判追责。本书则用规则与标准来进行类似区分，规则是明确可执行的，而标准则是结果导向的，遵守规则是可能达不到标准的，这个事实是需要接受的。

此外，本书一个新知识点是相关系数与一致性比率的关系，这个非常类似谢林隔离模型。简单说一致性比率就是预测与结果符合的比率，相关性则是统计上的相关系数或共用因素。相关性为零时，一致性比率是50%，也就是瞎猜水平。相关性0.2，一致性水平56%，而相关性到0.6，一致性水平就会到71%。这里最重要的点在于瞎猜那50%的一致性水平，也就是很多决策的基线如果用成功失败看往往本来就有一半成功率，很多成功学大师却让你产生如果不按他说的做成功率就是0。根据本书里提到的综述研究，社会心理学效应大概只有0.2的相关性，也就是你看到的心理学研究进展产生的一致性比率大概比瞎猜也就好不多而已，但却可能被很多人奉为真理。

本书提到了很多消除噪音的方法，但在我看来其实还是识别噪音来源变成偏差的方法，如果你精读过《思考，快与慢》会发现这本书更像是DLC，而且别忘了《思考，快与慢》本身也存在一些争议。根本上噪音就是很难消除的，这里面有成本问题，也有人对自己决策普遍自信的问题。基本上这书读了跟没读差不多，但如同那个白大褂综合症，很多时候一些问题并不需要你找到真实对策，只要你能找到原因并接纳不确定性的存在，这个问题便解决了。