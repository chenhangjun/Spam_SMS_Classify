import csv
import numpy as np
import re
from zhon.hanzi import punctuation
import jieba
import pandas as pd

# 读取数据
csvFile = open("dataset.csv", "r")
reader = csv.reader(csvFile)
# type(reader) == _csv.reader
rows = [row for row in reader]
# type(rows) == list
data = np.array(rows)
# type(data) == numpy.ndarray
# data.shape == (50000, 2)
# 第一列为标签，第二列为短信内容
# 获取短信内容（文本）
text = data[:,1]
# type(text.element) == numpy.str_

# words 存放jieba分词结果 type(words_temp) == list
words = []

# 根据原始分词得到的高频停用词
stop_words = ['有', '和', '是', '在', '我', '了', '的']

remove_chars = '[0-9’a-zA-Z!"#$%&\'()*\\\\+,-./:;<=>?@?★…‘’[\\]^_`{|}~(\s*)]+'
# 逐行去除特殊字符、数字英文（地址链接）和标点
for i in range(0, len(text)):
  newstr = re.sub(remove_chars, '', text[i])
  text[i] = re.sub("[{}]+".format(punctuation), "", newstr)
  # print(text[i])
  # 进行分词/
  # words.append(jieba.lcut(text[i]))   # 不管停用词，直接添加
  list_words = jieba.lcut(text[i])
  for word in list_words:
    if word in stop_words:
      list_words.remove(word)
  words.append(list_words)

# print(len(words[0]))

with open('words.csv','w',newline='') as f:
    writer=csv.writer(f)
    for word in words:
        data=','.join(word)
        writer.writerow([data])

# data_in = pd.DataFrame(words)
# try:
#     # csv_headers = ['sentence']
#     data_in.to_csv('words.csv', header=False, index=False, mode='a+', encoding='utf-8')
#
# except UnicodeEncodeError:
#     print("编码错误, 该数据无法写到文件中, 直接忽略该数据")