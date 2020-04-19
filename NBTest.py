import numpy as np
import csv
from NaiveBayes import NaiveBayes
import matplotlib.pyplot as plt

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

x_axis = np.zeros(1001)
accuracy = np.zeros(1001)
precision = np.zeros(1001)

# str = 0.45
# end = 0.50


# for i in range(0, 1001):
#   para = str + (end - str) * 0.001 * i
  # print("para = %f" %(para))
  # x_axis[i] = para

para = 0.4743
NB = NaiveBayes()
NB.fit(X_train, Y_train, para)

count = 0 
PSpam = 0
TSpam = 0

for j in range(0, len(Y_test)):
  tag = NB.predict(X_test[j])
  if Y_test[j] == tag:
    count += 1
  # 1为spam, 0为ham，与标签一致
  if tag == 1:
    PSpam += 1
    if Y_test[j] == 1:
      TSpam += 1
  # else:
  #   print(X_test[j], i, tag)

length = len(Y_test)

print("With Laplacial correction")
print("Threshold is %f" % para)
print("准确率： %.2f%%  查准率： %.2f%%" %(((count / length) * 100),((TSpam / PSpam) * 100)))

'''
  accuracy[i] = count / length * 100
  if TSpam == 0:
    precision[i] = 0
  else:
    precision[i] = TSpam / PSpam * 100
  


# sub_axix = filter(lambda x: x % 200 == 0, x_axis)
# plt.title('NaiveBayes--Laplacian correction')
plt.title('NaiveBayes--without Laplacian correction')
plt.plot(x_axis, accuracy, color='red', label='accuracy')
plt.plot(x_axis, precision, color='blue', label='precision')
plt.legend()  # 显示图例

plt.xlabel('threshold')
plt.ylabel('percentage')
plt.show()
'''
