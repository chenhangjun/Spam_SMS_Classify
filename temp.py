import numpy as np
import csv


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



N1 = int(len(words) * 0.8)
X_train = words[0 : N1]

all_map = dict()    # 词频统计
all_words = list()  # 词语列表

# 所有分词都放入all_words，包含重复
for items in X_train:
  for word in items:
    all_words.append(word)

for word in all_words:
  all_map[word] = all_map.setdefault(word, 0) + 1


# 交换key-value，便于按value排序
items=all_map.items()
backitems=[[v[1],v[0]] for v in items]
# 按现key排序
backitems.sort()

print(backitems)

# with open('dict.csv', 'w', newline='') as f:
#   writer = csv.writer(f)
#   for item in backitems:
#     writer.writerow(item)