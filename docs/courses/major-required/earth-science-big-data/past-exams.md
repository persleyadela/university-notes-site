# 历年卷
本页收集地球科学大数据课程的历年考试题，仅供课程复习参考，英文题目既可以用中文回答也可以用英文。（注：本资料来自cc98各前辈的回忆整理）

## 2025–2026 春夏
按知识点排序：


1. 请给出至少三种数据编码方式，分别说明其基本思想、特征及适用场景。
2. 什么是模型的过拟合？请给出至少三条缓解过拟合的策略。
3. RNN 循环神经网络中梯度消失的原因是什么？LSTM 是如何解决这一问题的？
4. 什么是 GNN（图神经网络）？请简述其消息传递范式。
5. 请列举机器学习在短期气候预测中面临的关键难题与挑战。
6. 模型的可解释性为何重要？请介绍 SHAP 的基本原理。
7. 传统机器学习方法（如 RF 和 SVM）与深度学习方法（以卷积神经网络 CNN 为代表），请从特征提取方式、对数据量的依赖以及模型可解释性三个方面分析二者的区别。
8. 如何将通用大模型应用于垂直领域？请给出至少三种方法。
9. 以下是一段 Transformer 模块的代码，请回答：

```
class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, num_classes):
        super(SimpleTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.attention = nn.MultiheadAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            batch_first=True
        )
        self.fc = nn.Linear(embed_dim, num_classes)
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        attn_output, attn_weights = self.attention(x, x, x)
        logits = self.fc(pooled)
        return logits

```

(1) `Embedding`、`attention`、`fc` 这三个模块的作用分别是什么？

(2) `attention(x, x, x)` 中三个 `x` 的含义分别是什么？

(3) `num_heads` 是什么参数？为什么要使用多头注意力而不是单头注意力？

10.（英文题）结合冰川 SMS 案例（也可结合深层海洋流速的案例）回答：

(1) 如果将数据随机打乱后再划分训练集和测试集，模型的表现会好得多，但这存在什么问题？正确的数据划分方式是什么？

(2) 在极端值的预测上，神经网络 NN 的表现通常比线性回归 LR 要好得多，这是为什么？这对我们进行模型选型有什么启示？


## 2024-2025春夏
1.支持向量机SVM的核心思想是什么？在线性可分和非线性可分的情况下，SVM分别该如何处理？
2.卷积神经网络CNN的基本结构、原理和特点。举3个CNN在地球科学中（或者“遥感中”）的典型应用。
3.在数据驱动的应用中，有100个独立样本，说明你在建模中样本的使用策略。
4.大气是混沌的，为何气候具有可预测性？
5.ConvLSTM和LSTM相比，结构有什么不同？有什么优势？
6.解释梯度消失和梯度爆炸。发生梯度消失和梯度爆炸的原因是什么？有什么解决途径？
7.智能体（Agent）的概念是什么？有哪些核心模块？试举一个生活中的应用例子解释。
8.有一段全连接神经网络如下：（是FCNet，不是FCN）
class FCNet(nn.Module):
    def __init__(self):
        super(FCNet, self).__init__()
        self.fc1 = nn.Linear(10, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 10)   

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)              
        x = self.fc2(x)
        x = self.relu(x)           
        x = self.fc3(x)
        return x


请问这段神经网络的层结构是怎样的？各层的作用以及适用于哪些任务？
9.（英文，最好英文作答）
In both cryosphere and oceanography lectures, the common challenges for machine learning was relating sparse,high-quality measurements to widespread but indirect remote sensing data.
a)For the application of estimating a glacier's SMB,with a ML regression model,describe the data needed(input features and output labels).What are the challenges for acquiring or using those data?
b)Similarly,let's say we want to estimate the deep ocean velocity at 1000 meters from surface data.describe the data needed and what are the challenges for acquiring or using those data.

## 2023-2024春夏
1\. ConvLSTM是什么？ConvLSTM的结构是什么？相对于LSTM的优点。（ConvLSTM和LSTM的区别）(8分)

2\. 如何测量地球体系内的液体体积和质量？如果已知某种物质，想要根据化学平衡计算另一种物质，用到什么类别的机器学习方法？(8分)

3.(英) 为什么利用p波和s波可以定位地震？使用这种技术定位地震的要求？我们可以从地震位置中学习到什么信息或知识？(8分)

4.(英) 基于sparse-enforcing penalty的多元线性回归在动态变化过程中的应用。举两例说明。(8分)
![](%E5%8E%86%E5%B9%B4%E5%8D%B7/image.png)
5\. 五折交叉验证的原理、特点、优势。使用五折交叉验证得到的模型如何应用。(8分)

6\. 模型选型，模型评价，模型优化的功能和目标。对每个过程用一个具体的方法例子说明其原理。(10分)

7\. 回归模型中的欠拟合和过拟合是什么？分别说明回归模型可能存在什么问题？分别如何改善？(10分)

8\. 假如观测精度不断提高，观测资料质量不断提升，数值模式动力和物理过程不断完善，预报的有效时长是否可以无限增加？(10分)

9\. 基于深度学习框架，如何对城市轨迹数据进行时空模式挖掘？可能挖掘出哪些时空模式？(15分)

10\. 给一段神经网络代码，LSTM，分析神经网络层结构，每层的作用。这个神经网络适用于什么任务。(有卷积层，池化层，线性层)(15分)



## 2022-2023
该次题目由于课程后面换老师教了可能参考价值低一些

1、模型选取，模型评价，模型优化的功 能和目标是什么，各举一例说明 

2，列举三种空间回归方法，它们各自的 特点和优缺点 

3，地球科学发展前沿的趋势是什么 

4，什么是过拟合，什么是欠拟合，结合 画图说明 

5，如何计算地球上液体的体积和质量？ 如果用化学平衡方程式计算液体中的元 素，用什么机器学习方法？ 

6，（英文）如何用卫星计算海洋表面流 速，如何用表面流速重构（reconstruct current speed) 海面下流速？重构需要 
用到什么数据 

7，（英文）举两个例子说明卫星如何监 视冰川活动 

8，长短期记忆网络（LSTM）的结构是什 么，它如何解决RNN的记忆问题？ 

9，空间轨迹数据的聚类分析可以获得什 么信息？有什么作用？ 

10，利用机器学习进行气候预测存在的问题 
