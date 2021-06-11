import pandas as pd
#from mysql3 import *
from library import *
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Integer,String
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import datetime
import sys
engine = create_engine('mysql+pymysql://root:wanyanfei123@localhost:3306/library2')
sql_query = 'select * from books;'
plt.rcParams['font.sans-serif'] = ['SimHei']
Session_class = sessionmaker(bind=engine)
session = Session_class()
# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
# 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
def check():
    print('请输入想查询的书籍分布：\n语言（language）,类别（category），作者（author），货物（goods），出版社（press）：')
    print('查询书籍被借情况：（bor）')
    Check = input()
    if(Check == 'language'):
        lan = Language.query.all()
        j = 0
        k = 0
        y = []
        x = []
        for l in lan:
            b = Book.query.filter(Book.Language_id == l.id)
            for i in b:
                print(l.language_name,i.name)
                j = j+1
            y.append(j)
            j = 0
            k = k+1
            x.append(l.language_name)
        plt.plot(x, y, color = 'red',linestyle ='-.')
        plt.show()
    elif(Check == 'category'):
        cat = Category.query.all()
        j = 0
        k = 0
        y = []
        x = []
        for l in cat:
            b = Book.query.filter(Book.Category_id == l.id)
            for i in b:
                print(l.category_name, i.name)
                j = j + 1
            y.append(j)
            j = 0
            k = k + 1
            x.append(l.category_name)
        plt.plot(x, y, color='red', linestyle='-.')
        plt.show()
    elif(Check == 'author'):
        aut = Author.query.all()
        j = 0
        k = 0
        y = []
        x = []
        for l in aut:
            b = Book.query.filter(Book.Author_id == l.id)
            for i in b:
                print(l.author_name, i.name)
                j = j + 1
            y.append(j)
            j = 0
            k = k + 1
            x.append(l.author_name)
        plt.plot(x, y, color='red', linestyle='-.')
        plt.show()
    elif(Check == 'press'):
        pre = Press.query.all()
        j = 0
        k = 0
        y = []
        x = []
        for l in pre:
            b = Book.query.filter(Book.Press_id == l.id)
            for i in b:
                print(l.press_name, i.name)
                j = j + 1
            y.append(j)
            j = 0
            k = k + 1
            x.append(l.press_name)
        plt.plot(x, y, color='red', linestyle='-.')
        plt.show()
    elif(Check == 'goods'):
        boo = Book.query.all()
        j = 0
        k = 0
        y = []
        x = []
        for l in boo:
            b = Goods.query.filter(Goods.Goods_id == l.id)
            for i in b:
                print('书名：',l.name,'书号：' ,i.id)
                j = j + 1
            y.append(j)
            j = 0
            k = k + 1
            x.append(l.name)
        plt.plot(x, y, color='red', linestyle='-.')
        plt.show()
    elif (Check == 'bor'):
        boo = BORROW.query.all()
        j = 0
        k = 0
        y = []
        x = []
        SORT = []
        num = {}

        for l in boo:
            SORT.append(l.Book_id)
        sort_set = set(SORT)
        for item in sort_set:
            num[Book.query.get(item).name] = SORT.count(item)
        print(num)
        num = sorted(num.items(),key=lambda x:x[1],reverse= True)
        print(num)
        for k in num:
            j = j + 1
            x.append(k[0])
            y.append(k[1])
            if j == 30:
                break
        plt.plot(y, x, color='blue', linestyle='-.')
        plt.show()
def Add():
    while True:
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        name = input('书名：')
        cn = input('类别：')
        pn = input('出版社：：')
        an = input('作者：')
        ln = input('语言：')
        value = input('价格：')
        number = input('数量：')
        aut = Author.query.filter(Author.author_name == an).first()
        lan = Language.query.filter(Language.language_name == ln).first()
        pre = Press.query.filter(Press.press_name== pn).first()
        cat = Category.query.filter(Category.category_name==cn).first()
        if not aut:
            a = Author(
                author_name=an
            )
            session.add(a)
            session.commit()
        if not lan:
            l = Language(
                language_name=ln
            )
            session.add(l)
            session.commit()
        if not pre:
            p = Press(
                press_name=pn
            )
            session.add(p)
            session.commit()
        if not cat:
            c = Category(
                category_name= cn
            )
            session.add(c)
            session.commit()
        # if aut and lan and pre and cat:
        newform = Book(
            name=name,
            time=time,
            value=value,
            number=number,
            author_id = a.id,
            Category_id = c.id,
            Press_id = p.id,
            Language_id = l.id
        )
        session.add(newform)
        session.commit()
        '''g = Goods(
            Goods_id = newform.id
        )'''
        for i in range(int(number)):
            g = Goods(
                Goods_id=newform.id
            )
            session.add(g)
            session.commit()
        over = input('结束输入:yes')
        if over == 'y' or 'yes':
            break

def Borrow(_r):
    n = input('书名：')
    #c = input('类型：')
    #a = input('作者：')
    s = Book.query.filter(n == Book.name).first()
    #print(s.id)

    if s == None:
        print('未找到此书')
    else:
        goo = Goods.query.filter(s.id == Goods.Goods_id).first()
        if goo != None:
            session.query(Goods).filter(goo.id == Goods.id).delete()
            session.commit()
            b = BORROW(
                time=datetime.datetime.now().strftime('%Y-%m-%d'),
                Register_id=_r.id,
                Book_id=s.id
            )
            session.add(b)
            session.commit()
            if input('借书成功,是否返回菜单（y/n）') == 'n':
                Borrow(_r)
            else:
                SignIn()

        else:
            print('此书已被借完,返回菜单：')
            # 如果没货了，就删掉书表中的字段，删之前看看其他表中信息还在不在
            if Category.query.filter(s.Category_id == Category.id).first() == None:
                caa = Category.query.filter(s.Category_id == Category.id)
                session.query(Category).filter(caa.id == Category.id).delete()
                session.commit()
            if Author.query.filter(s.author_id == Author.id).first() == None:
                auu = Author.query.filter(s.author_id == Author.id)
                session.query(Author).filter(auu.id == Author.id).delete()
                session.commit()

            if Press.query.filter(s.Press_id == Press.id).first() == None:
                prr = Press.query.filter(s.Press_id == Press.id)
                session.query(Press).filter(prr.id == Press.id).delete()
                session.commit()

            if Language.query.filter(s.Language_id == Language.id).first() == None:
                laa = Language.query.filter(s.Language_id == Language.id)
                session.query(Language).filter(laa.id == Language.id).delete()
                session.commit()
            session.query(Book).filter(s.id == Book.id).delete()
            session.commit()
            SignIn()

def SignIn():
    I =input('注册（signin）登录（signup），退出(exit)')
    if I== 'signin':
        N = input('用户名：')
        P = input('密码：')
        u = User(
            user_name = N,
            user_password = P
        )
        session.add(u)
        session.commit()
        print('注册成功，请登录')
        SignUp()
    elif I == 'signup':
        print('请登录')
        SignUp()
    elif I == 'exit':
        print('已退出')
        sys.exit()
def SignUp():
    N = input('用户名：')
    P = input('密码：')
    _r = Register(
        register_name=N,
        register_password=P
    )
    session.add(_r)
    session.flush()
    session.commit()
    print(_r.id)
    print('登录成功，借书：（borrow），查看图书信息（check），图书入库（add）')
    use = input()
    if use == 'check':
        check()
    elif use == 'add':
        Add()
    elif use == 'borrow':
        Borrow(_r)

SignIn()

#Borrow()