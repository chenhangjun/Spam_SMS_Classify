from tkinter import *
import json
import math
from zhon.hanzi import punctuation
import jieba


class MainPage(object):

  def __init__(self, master=None):

    self.content = ''
    self.result = ''
    self.root = master  # 定义内部变量root
    self.root = Tk(className='垃圾短信识别')  # 窗口标题
    self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
    self.root.resizable(0, 0)
    # 输入框
    self.text_1 = Text(self.root, width=62, height=12)
    # label 3 显示结果
    self.label_3 = Label(self.root)
    self.createPage()
    self.ham_map, self.spam_map = self.ReadModel('modeldict.json')


  def createPage(self):

    # 添加一个label
    self.page = Frame(self.root)  # 创建Frame
    self.page.pack()
    Label(self.page).grid(row=0, stick=W)

    '''
    Label(self.page, text='输入短信').grid(row=1, column=1, stick=W)
    Entry(self.page, textvariable=self.content, width=70).grid(row=3, column=1)
    Label(self.page, text='判定结果为：').grid(row=5, stick=W, pady=10)
    Label(self.page, text=self.result).grid(row=5, stick=W, pady=10)
    Button(self.page, text='判定', command=self.Judge).grid(row=5, column=7, stick=W)
    '''
    # 添加一个label
    label_1 = Label(self.root)
    label_1['text'] = '输入短信:'
    label_1.place(x=50, y=50)

    self.text_1.place(x=50, y=90)

    # label 2
    label_2 = Label(self.root)
    label_2['text'] = '判定结果为:'
    label_2.place(x=50, y=320)


    self.label_3.place(x=130, y=320)

    # button
    button = Button(self.root, text='判定', command=self.Judge)
    button.place(x=500, y=310)


  def Judge(self):

    # 获取输入内容
    sentence = self.text_1.get('0.0', 'end')
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
    tag = self.Predict(list_words)
    # 修改标签显示
    if tag == 1:
      self.result = '垃圾邮件'
    else:
      self.result = '正常邮件'

    self.label_3['text'] = self.result


  def Predict(self, text):


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
      ham_pro += math.log((self.ham_map.get(word, 0) + 1) / (ham_words_count + words_set_size))
      spam_pro += math.log((self.spam_map.get(word, 0) + 1) / (spam_words_count + words_set_size))

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


  def ReadModel(self, filename):

    with open(filename) as f:
      dictObj = json.load(f)
      ham_map = dictObj['ham']
      spam_map = dictObj['spam']

    return ham_map, spam_map



