---
title: 线性模型
author: ''
date: '2020-10-12'
slug: linear-model
categories: []
tags: []
---

线性模型的基本形式就是因变量是由自变量作用加和而成，在这个语境下，其实把自变量改为变量，放宽独立性限制，也能将一些非线性部分，例如高幂次的自变量及变量间的乘积或交互作用考虑进去，这样，线性模型几乎可以覆盖绝大多数科研中常用的假设检验与模型。在实际问题的抽象上，只要可以把目标数值的变动用其他数值的拆解或组合表示出来，那么可以粗略认为标准化后其他数值的回归系数可用来比较不同数值间的贡献，而对于该系数的显著性检验则可以说明该系数的影响是否显著。

打个比方，流行病学里常说的某种疾病发病率或风险比在考虑了人群性别、年龄、BMI、吸烟史等的影响后发现某污染物起了显著影响，这就是说在一个目标变量为病发病率或风险比的线性模型中，性别、年龄、BMI、吸烟史作为协变量而污染物作为自变量，模型拟合结束后发现污染物的系数经假设检验为显著差异于零，也就是没影响。这里，协变量与自变量在回归上是平等的，可以把协变量理解为控制变量，如果你考察吸烟的影响，那么吸烟与否就是自变量，包含污染物在内其他项就成了协变量。不过所有考察变量选择的原则在于其理论上或经验上被认为与目标变量有关系且无法通过随机采样、配对等手段消除影响，这种情况对于观测数据比较常见。

当线性模型的自变量只有一项时，其实考察的就是自变量与响应变量间的相关性。当自变量为多项时，也就是多元线性回归，考察的是你自己定义的“自变量”与“协变量”还有响应变量的关系。如果自变量间不能互相独立，那么最好将独立的部分提取出来作为新的变量，这种发现潜在变量的过程归属于因子分析，可以用来降维。自变量本身存在随机性，特别是个体差异，这种随机性可能影响线性模型自变量的系数或斜率，也可能影响线性模型的截距，甚至可能同时影响，此时考虑了自变量的随机性的模型就是线性混合模型。线性混合模型其实已经是层级模型了，自变量的随机性来源于共同的分布。如果自变量间存在层级，例如有些变量会直接影响其他变量，那么此时线性模型就成了决策/回归树模型的特例了。如果层级关系错综复杂，那不依赖结构方程模型是没办法搞清楚各参数影响的。然而模型越复杂，对数据的假设就越多，对样本量的要求也就越高。同时，自变量或因变量有些时候也要事先进行连续性转换，这就给出了logistics回归、生存分析等特殊的回归模型。科研模型如果是依赖控制实验的，那么会在设计阶段随机化绝大部分变量，数据处理方面到线性混合模型就已经很少见了。但对于观测数据，线性混合模型只是起点，对于侧重观察数据的社会科学研究，样本量与效应大小是结论可靠性的关键，精细的模型无法消除太多的个体差异。

高维数据是线性模型的一大挑战，当维度升高后，变量间要么可能因为变异来源相似而共相关，要么干脆就是随机共相关。在某些场景下，高维数据可能都没有目标变量，需要先通过探索性数据分析找出样本或变量间的组织结构。这种场景下应通过变量选择过程来保留独立且与目标变量有潜在关系的变量。也就是说，变量选择的出发点是对数据的理解，优先考虑相关变量而非简单套用统计分析流程。当然，统计方法上也有变量选择的套路，评判标准可能是信息熵或模型稳健度的一些统计量，可以借助这些过程来简化模型或者说降维。对于线性模型而言，就是均方误、Mallow’s $C_p$、AIC、BIC还有调节R方等，可借助回归模型软件来完成。

回归或模型拟合都存在过拟合的风险，所谓过拟合，就是模型对于用来构建模型的数据表现良好，但在新数据的预测性上却不足的情况。与过拟合对应的是欠拟合，此时拟合出的模型连在构建模型的数据验证上表现都不好。这里的表现可以用模型评价的一些指标，其实跟上面进行变量选择的指标是一样的，好的模型应该能捕捉到数据背后真实的关系，也因此在训练数据与新数据上表现一致。

在统计学习领域里，工程实践上最简单的验证过拟合与欠拟合的方法就是对数据进行切分，分为用来构建模型的训练集与验证模型预测性能的检测集，更细的分法则将检测集分为可在模型调参过程中使用多次的检测集与最后最终评价模型的一次性验证集，三者比例大概6:3:1，也可根据实际情况来定。也就是说，模型的构建不是一次性完成的，而是一个反复调整模型参数的过程来保证最终的模型具备良好的预测性与稳健度。

在技术层面上，调参过程有两种基本应对方法，第一种是重采样技术，第二种是正则化，两种方法可以组合使用。重采样技术指的是通过对训练集反复采样多次建模来调参的过程。常见的重采样技术有留一法，交叉检验与bootstrap。留一法在每次建模留一个数据点作为验证集，重复n次，得到一个CV值作为对错误率的估计。交叉检验将训练集分为多份，每次建模用一份检验，用其他份建模。bootstrap更可看作一种思想，在训练集里有放回的重采样等长的数据形成新的数据集并计算相关参数，重复多次得到对参数的估计，计算标准误。在这些重采样技术中，因为进行的多次建模，也有多次评价，最佳的模型就是多次评价中在验证集上表现最好的那一组。

正则化则是在模型构建过程中在模型上对参数的效应进行人为减弱，用来降低过拟合风险。具体到线性模型上，就是在模型训练的目标上由单纯最小化均方误改为最小化均方误加上一个对包含模型参数线性组合的惩罚项，这样拟合后的模型参数对自变量的影响就会减弱，更容易影响不显著，如果自变量过拟合的话就会被这个正则化过程削弱。当惩罚项为模型参数的二次组合时，这种回归就是岭回归；当惩罚项为模型参数的一次绝对值组合时，这种回归就是lasso；当惩罚项为一次与二次的组合时，这种回归就是弹性网络回归。实践上正则化过程对于降低过拟合经常有神奇效果，同时正则化也可作为变量选择的手段，虽然岭回归无法将系数惩罚为0，但lasso可以，这样在参数收缩过程中也就同时实现了变量选择。

为了说明实际问题，有时候单一形式的模型是不能完全捕捉数据中的变动细节的，我们可以在工程角度通过模型组合来达到单一模型无法达到的预测性能。模型组合的基本思想就是对同一组数据生成不同模型的预测结果，然后对这些结果进行二次建模，考虑在不同情况下对不同模型预测结果给予不同的权重。这种技术手段可以突破原理限制，而最出名的例子就是人工神经网络里不同神经元采用不同核函数的做法了。

对于科研数据的线性回归，还有两个常见问题，一个是截断问题，另一个是缺失值处理。截断问题一般是采样精度或技术手段决定的，在数值的高位或低位无法采集高质量数据，此时可以借助截断回归等统计学方法来弥补。另一种思路则是在断点前后构建不同的模型，这样分别应对不同质量的数据。对于数据缺失值的问题，统计学上也提供了很多用来删除或填充缺失值的方法，填充数据不应影响统计推断，越是接近的样本，就越是可以用来填充缺失值，当然这个思路反着用就是个性化推荐系统模型的构建了。