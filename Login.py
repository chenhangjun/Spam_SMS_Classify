from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from SignUp import *
import pymysql



class Login(object):

  def __init__(self, master=None):

    self.db = pymysql.connect("localhost", "chenhangjun", "1030416518", "InfoDB", charset='utf8')
    self.cursor = self.db.cursor()

    self.root = master  # 定义内部变量root
    self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
    self.username = StringVar()
    self.password = StringVar()
    self.createPage()


  def createPage(self):

    self.page = Frame(self.root)  # 创建Frame
    self.page.pack()
    Label(self.page).grid(row=0, stick=W)
    Label(self.page, text='账号: ').grid(row=1, stick=W, pady=10)
    Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
    Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
    Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
    Button(self.page, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
    Button(self.page, text='注册', command=self.signUp).grid(row=3, column=1, stick=E)


  def loginCheck(self):

    name = self.username.get()
    pwd1 = self.password.get()

    if name == '':
      showinfo(title='错误', message='请输入账号！')
    elif pwd1 == '':
      showinfo(title='错误', message='请输入密码！')
    else:
      sql = "SELECT PASSWORD FROM USER WHERE USER_NAME = '%s'" % (name)

      try:
        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取所有记录列表
        pwd2 = self.cursor.fetchall()  # pwd2 为 tuple， (("pwd", ), )

        if pwd2 == ():
          showinfo(title='错误', message='账号不存在！')
        elif pwd1 == pwd2[0][0]:
          self.db.close()
          MainPage(self.root)
          self.root.destroy()

        else:
          showinfo(title='错误', message='密码错误！')

      except:
        print("except")
        self.db.close()


  def signUp(self):

    # self.root.withdraw()
    SignUp(self.root)
    # print("signup")
    # self.root.destroy()

