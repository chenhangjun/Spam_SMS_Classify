import math

# 参考：https://www.cnblogs.com/liweiwei1419/p/9870956.html

class NaiveBayes:

  def __init__(self):

    self.ham_count = 0    # 非垃圾短信数量
    self.spam_count = 0   # 垃圾短信数量

    self.ham_words_count = 0    # 非垃圾短信总次数
    self.spam_words_count = 0   # 垃圾短信总词数

    self.ham_words = list()     # 非垃圾短信词语列表
    self.spam_words = list()    # 垃圾短信词语列表

    self.words_set = set()    # 两类短信所有词语的集合，不重复
    self.words_set_size = 0

    self.ham_map = dict()     # 非垃圾短信词频统计
    self.spam_map = dict()    # 垃圾短信词频统计

    # 先验概率 P(c)
    self.ham_probability = 0
    self.spam_probability = 0

  def fit(self, X_train, Y_train):
    self.build_words_set(X_train, Y_train)
    self.word_count()


  # 建立单词集合
  def build_words_set(self, X_train, Y_train):

    for words, y in zip(X_train, Y_train):
      if y == 0:
        # 非垃圾短信
        self.ham_count += 1
        self.ham_words_count += len(words)
        for word in words:
          self.ham_words.append(word)
          self.words_set.add(word)
      if y == 1:
        # 垃圾短信
        self.spam_count += 1
        self.spam_words_count += len(words)
        for word in words:
          self.spam_words.append(word)
          self.words_set.add(word)

    self.words_set_size = len(self.words_set)


  # 统计词频并计算先验概率
  def word_count(self):

    # 统计各类中各词的频次
    for word in self.ham_words:
      # 默认初值为0
      self.ham_map[word] = self.ham_map.setdefault(word, 0) + 1

    for word in self.spam_words:
      self.spam_map[word] = self.spam_map.setdefault(word, 0) + 1

    # 【下面两行计算先验概率】
    # 非垃圾短信的概率
    self.ham_probability = self.ham_count / (self.ham_count + self.spam_count)
    # 垃圾短信的概率
    self.spam_probability = self.spam_count / (self.ham_count + self.spam_count)


  def predict(self, sentence_words):

    # 基于词袋模型的朴素贝叶斯算法; 多项式模型的平滑/拉普拉斯平滑
    # P(x_i|c) = P(“某个词”|c) = (c类短信中出现“某个词”的次数的总和+1) /
    # c类短信中所有词出现次数（计算重复次数）的总和 + 总不重复的词语数量

    ham_pro = 0
    spam_pro = 0

    for word in sentence_words:
      ham_pro += math.log((self.ham_map.get(word, 0) + 1) / (self.ham_count + self.words_set_size))
      spam_pro += math.log((self.spam_map.get(word, 0) + 1) / (self.spam_count + self.words_set_size))

    ham_pro += math.log(self.ham_probability)
    spam_pro += math.log(self.spam_probability)

    # 1为spam, 0为ham，与标签一致
    return int(spam_pro >= ham_pro)