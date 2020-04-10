import numpy as np
import csv
from NaiveBayes import NaiveBayes

# 读取数据
csvFile = open("dataset.csv", "r")
reader = csv.reader(csvFile)
rows = [row for row in reader]
data = np.array(rows)
# 获取标签
Y_data_str = data[:, 0]

Y_data_int = np.zeros(len(Y_data_str), dtype=int)

# Y_data_str 值的类型从字符转化为int
for i in range(0, len(Y_data_str)):
  Y_data_int[i] = int(Y_data_str[i])


# 获取短信分词
csvFile = open("words.csv", "r")
reader = csv.reader(csvFile)
rows = [row for row in reader]
data = np.array(rows)
# data.shape == (50000, 1)
data = data[:,0]
# ==> data.shape == (50000,)

words = []
for obj in data:
  words.append(obj.split(','))
# len(words) == 50000



N1 = int(len(Y_data_int) * 0.8)

#数据集按4:1 划分为训练集：测试集
Y_train = Y_data_int[0 : N1]
X_train = words[0 : N1]
Y_test = Y_data_int[N1 : len(Y_data_int)]
X_test = words[N1: len(words)]


NB = NaiveBayes()
NB.fit(X_train, Y_train)

count = 0
for i in range(0, len(Y_test)):
  tag = NB.predict(X_test[i])
  if Y_test[i] == tag:
    count += 1
  # else:
  #   print(X_test[i], i, tag)

length = len(Y_test)
print("%.2f%%" %((count / length) * 100))