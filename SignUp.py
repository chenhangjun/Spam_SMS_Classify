from tkinter import *
from tkinter.messagebox import *
import pymysql


class SignUp(object):

  def __init__(self, master=None):

    self.db = pymysql.connect("localhost", "chenhangjun", "1030416518", "InfoDB", charset='utf8')
    self.cursor = self.db.cursor()

    self.root = master  # 定义内部变量root
    self.root = Toplevel()
    self.root.title("注册")
    self.root.geometry('%dx%d' % (400, 250))  # 设置窗口大小
    self.username = StringVar()
    self.password1 = StringVar()
    self.password2 = StringVar()
    self.createPage()


  def createPage(self):

    self.page = Frame(self.root)  # 创建Frame
    self.page.pack()
    Label(self.page).grid(row=0, stick=W)
    Label(self.page, text='账号: ').grid(row=1, stick=W, pady=10)
    Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
    Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
    Entry(self.page, textvariable=self.password1, show='*').grid(row=2, column=1, stick=E)
    Label(self.page, text='重复密码: ').grid(row=3, stick=W, pady=10)
    Entry(self.page, textvariable=self.password2, show='*').grid(row=3, column=1, stick=E)
    Button(self.page, text='确定', command=self.confirm).grid(row=4, stick=W, pady=10)
    Button(self.page, text='取消', command=self.pageQuit).grid(row=4, column=1, stick=E)


  def pageQuit(self):

    self.db.close()
    self.root.destroy()


  def confirm(self):

    name = self.username.get()
    pwd1 = self.password1.get()
    pwd2 = self.password2.get()

    if name == '':
      showinfo(title='错误', message='请填写账号！')
    elif pwd1 == '':
      showinfo(title='错误', message='请填写密码！')
    elif pwd2 == '':
      showinfo(title='错误', message='请重复密码！')
    elif pwd1 != pwd2:
      showinfo(title='错误', message='两次密码输入不一致！')
    else:
      sql1 = "SELECT * FROM USER WHERE USER_NAME = '%s'" % (name)
      sql2 = "INSERT INTO USER(USER_NAME, PASSWORD) VALUES('%s', '%s')" % (name, pwd1)

      self.cursor.execute(sql1)
      res = self.cursor.fetchall()

      if res != ():
        showinfo(title='错误', message='该账号已存在！')
      else:
        try:
          # 执行sql语句
          self.cursor.execute(sql2)
          # 提交到数据库执行
          self.db.commit()
          showinfo(title='恭喜', message='注册成功！')
        except:
          # 发生错误时回滚
          self.db.rollback()
          print("error")
        finally:
          self.db.close()
          self.root.destroy()
