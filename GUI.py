from tkinter import *
import json
import math
from zhon.hanzi import punctuation
import jieba

def ReadModel(filename):

  with open('modeldict.json') as f:
    dictObj = json.load(f)
    ham_map = dictObj['ham']
    spam_map = dictObj['spam']

  return ham_map, spam_map


def Predict(text):

  ham_map, spam_map = ReadModel('modeldict.json')
  ham_words_count = 323632
  spam_words_count = 97890
  ham_count = 35978
  spam_count = 4022
  words_set_size = 62133
  para = 0.4743

  ham_probability = ham_count / (ham_count + spam_count)
  spam_probability = spam_count / (ham_count + spam_count)

  ham_pro = 0.0
  spam_pro = 0.0

  for word in text:
    ham_pro += math.log((ham_map.get(word, 0) + 1) / (ham_words_count + words_set_size))
    spam_pro += math.log((spam_map.get(word, 0) + 1) / (spam_words_count + words_set_size))

  ham_pro += math.log(ham_probability)
  spam_pro += math.log(spam_probability)

  # 1为spam, 0为ham，与标签一致
  # return int(spam_pro >= ham_pro)
  tot = spam_pro + ham_pro
  threshold = tot * para
  if spam_pro >= threshold:
    return 1
  else:
    return 0


# 定义按钮点击事件
def on_click(input, label):

  # 获取输入内容
  sentence = input.get('0.0', 'end')
  # 分词
  stop_words = ['有', '和', '是', '在', '我', '了', '的']
  remove_chars = '[0-9’a-zA-Z!"#$%&\'()*\\\\+,-./:;<=>?@?★…‘’[\\]^_`{|}~(\s*)]+'
  newstr = re.sub(remove_chars, '', sentence)
  sentence = re.sub("[{}]+".format(punctuation), "", newstr)
  list_words = jieba.lcut(sentence)
  for word in list_words:
    if word in stop_words:
      list_words.remove(word)

  # 预测
  tag = Predict(list_words)
  # 修改标签显示
  if tag == 1:
    label['text'] = '垃圾邮件'
  else:
    label['text'] = '正常邮件'


def main():

  root = Tk(className = '垃圾短信识别')   # 窗口标题
  root.geometry('600x400')
  root.resizable(0, 0)


  # 添加一个label
  label_1 = Label(root)
  label_1['text'] = '输入短信:'
  label_1.place(x = 30, y = 50)

  # 输入框
  # text_1 = StringVar()
  # entry_1 = Entry(root)
  # entry_1['textvariable'] = text_1
  # entry_1.place(x = 50, y = 80, width = 500, height = 200)
  text_1 = Text(root, width = 62, height = 12)
  text_1.place(x = 50, y = 90)

  # label 2
  label_2 = Label(root)
  label_2['text'] = '判定结果为:'
  label_2.place(x = 50, y = 320)

  # label 3 显示结果
  label_3 = Label(root)
  # label_3['text'] = '垃圾邮件'
  label_3.place(x = 130, y = 320)

  # button
  button = Button(root, text = '判定', command = lambda: on_click(text_1, label_3))
  button.place(x = 500, y = 310)

  root.mainloop()


if __name__ == "__main__":
  main()