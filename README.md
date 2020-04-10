# Spam_SMS_Classify
一个中文文本分类项目 (NLP)



#### 数据集

------

来源：<https://github.com/hrwhisper/SpamMessage/tree/master/data/> 带标签数据集.txt

​	注：不确定这边来源的数据集是否是原创

说明：本项目选取了该数据集中的五万条数据作为训练/测试集dataset.csv，用python略作处理并转存了格式，未		   选取其中的异常样本（即含有希腊字母、日文等非常规字符的样本或由纯数字字母以及标点符号组成的样本）。

​	其中spam = 5041, ham = 44959，比例大约为1 : 9。