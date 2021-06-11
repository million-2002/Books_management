import time
from mysql3 import *
import string
import random
#作者模型
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)#主键
    author_name = db.Column(db.String(16), unique=False)
    #关系引用
    #books = db.relationship('Book', backref='author')
    #反向关联，查询books表，返回books—-obj，
    # books-obj。author找到books外键关联数据
    #查books返回authors
   # def __repr__(self):
    #    return 'Author :%s' % self.name
#货物
class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    Goods_id = db.Column(db.Integer,db.ForeignKey('books.id'))
'''
    def __repr__(self):
        return 'Goods :%s' % self.name
        '''
    #出版社
class Press(db.Model):
    __tablename__ = 'press'
    id = db.Column(db.Integer, primary_key=True)#主键
    press_name = db.Column(db.String(16), unique=False)
    #def __repr__(self):
     #   return 'Press :%s' % self.name
    #语言

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)#主键
    user_name = db.Column(db.String(16), unique=True)
    user_password = db.Column(db.String(16), unique=True)
class BORROW(db.Model):
    __tablename__ = 'borrow'
    id = db.Column(db.Integer, primary_key=True)#主键
    time = db.Column(db.String(16), unique=False)
    Register_id = db.Column(db.Integer,db.ForeignKey('register.id'))
    Book_id = db.Column(db.Integer,db.ForeignKey('books.id'))

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)#主键
    register_name = db.Column(db.String(16), unique=False)
    register_password = db.Column(db.String(16), unique=True)


class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)#主键
    language_name = db.Column(db.String(16), unique=False)
  #  def __repr__(self):
   #     return 'Language :%s' % self.name
    #类型
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)#主键
    category_name = db.Column(db.String(16), unique=False)
#    def __repr__(self):
 #       return 'Category :%s' % self.name
#书籍模型
class Book(db.Model):
    __tablename__ = 'books'
    name = db.Column(db.String(16), unique=False)
    time = db.Column(db.String(16), unique=False)
    id = db.Column(db.Integer, primary_key=True)# 主键
    value = db.Column(db.Integer, unique=False)
    number = db.Column(db.Integer, unique=False)

    #unique=True表示重复出现的记录只保存一条

    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
    Category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    Press_id = db.Column(db.Integer, db.ForeignKey('press.id'))
    Language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    #authors = db.relationship('Author',backref='author')



if __name__ == '__main__':
    db.drop_all() # 删除表
    db.create_all() # 创建表
    #往Author表里插数据
    a = []
    for i in range(50):
        a1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
        a.append(Author(author_name = a1))
    db.session.add_all(a)
    db.session.commit()
    us = []
    re = []
    for i in range(50):
        n = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6))
        p = ''.join(random.choice( string.digits) for _ in range(12))
        s = User(user_name = n,user_password = p)
        r = Register(register_name = n,register_password = p)
        us.append(s)
        re.append(r)
    db.session.add_all(us)
    db.session.commit()
    db.session.add_all(re)
    db.session.commit()
    c = []
    c.append(Category(category_name = '计科' ))
    c.append(Category(category_name = '心理学' ))
    c.append(Category(category_name = '社会学' ))
    c.append(Category(category_name = '哲学' ))
    c.append(Category(category_name = '历史学' ))
    c.append(Category(category_name = '文学' ))
    c.append(Category(category_name = '生物学' ))
    c.append(Category(category_name = '地理学' ))
    c.append(Category(category_name = '数学' ))
    db.session.add_all(c)
    db.session.commit()
    l = []
    l.append(Language(language_name='chinese'))
    l.append(Language(language_name='English'))
    l.append(Language(language_name='Russian'))
    l.append(Language(language_name='Latin'))
    l.append(Language(language_name='Japanese'))
    l.append(Language(language_name='Spanish'))
    l.append(Language(language_name='Arab'))
    db.session.add_all(l)
    db.session.commit()
    p = []
    p.append(Press(press_name='机械工业出版社'))
    p.append(Press(press_name='人民文学出版社'))
    p.append(Press(press_name='新华出版社'))
    p.append(Press(press_name='人民邮电出版社'))
    db.session.add_all(p)
    db.session.commit()

    b = []
    for i in range(100):
        n =  ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6))
        t1 = (2021,6,9,0,0,0,0,0,0)
        t2 = (2021,7,9,0,0,0,0,0,0)
        start = time.mktime(t1)
        end = time.mktime(t2)
        t= random.randint(start,end)
        ti = time.strftime("%Y-%m-%d",time.localtime(t))
        v =int(random.uniform(10, 600))
        a_id = int(random.uniform(1,50))
        c_id = int(random.uniform(1,9))
        p_id = int(random.uniform(1,4))
        l_id =int(random.uniform(1,7))
        b_ = Book(name=n, time=ti, value=v, number=1, author_id=a_id, Category_id=c_id, Press_id=p_id,
         Language_id=l_id)
        b.append(b_)

    db.session.add_all(b)
    db.session.commit()
    bo = []
    for i in range(100):
        t1 = (2021, 6, 9, 0, 0, 0, 0, 0, 0)
        t2 = (2021, 7, 9, 0, 0, 0, 0, 0, 0)
        start = time.mktime(t1)
        end = time.mktime(t2)
        t = random.randint(start, end)
        ti = time.strftime("%Y-%m-%d", time.localtime(t))
        borrow_ = BORROW(time = ti, Register_id = int(random.uniform(1,50)), Book_id =int(random.uniform(1,100)))
        bo.append(borrow_)
    db.session.add_all(bo)
    db.session.commit()
    #库存
    g= []
    for i in range(200):
        g.append(Goods(Goods_id= int(random.uniform(1,100))))
    db.session.add_all(g)

    db.session.commit()
    app.run(debug = True)