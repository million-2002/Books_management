from mysql3 import *
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

    def __repr__(self):
        return 'Goods :%s' % self.name
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
    user_name = db.Column(db.String(16), unique=False)
    user_password = db.Column(db.Integer, unique=True)
class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)#主键
    register_name = db.Column(db.String(16), unique=False)
    register_password = db.Column(db.Integer, unique=True)
class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)#主键
    language_name = db.Column(db.String(16), unique=True)
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
    '''
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
    Category_id = db.Column(db.Integer, db.ForeignKey('cagetory.id'))
    Press_id = db.Column(db.Integer, db.ForeignKey('press.id'))
    Language_id = db.Column(db.Integer, db.ForeignKey('language.id'))'''
    #authors = db.relationship('Author',backref='author')

#传入表单

if __name__ == '__main__':
    db.drop_all() # 删除表
    db.create_all() # 创建表
    #往Author表里插数据
    au1 = Author(author_name='老王')
    au2 = Author(author_name='老宋')
    au3 = Author(author_name='老刘')
    db.session.add_all([au1, au2, au3])
    db.session.commit()

    c1 = Category(category_name = '计算机' )
    c2 = Category(category_name = '心理学' )
    c3 = Category(category_name = '社会学' )
    c4 = Category(category_name = '哲学' )
    db.session.add_all([c1, c2, c3, c4])
    db.session.commit()

    l1 = Language(language_name = 'chinese' )
    l2 = Language(language_name = 'English' )
    l3 = Language(language_name = 'Russian' )
    l4 = Language(language_name = 'Latin' )
    db.session.add_all([l1, l2, l3, l4])
    db.session.commit()
    p1 = Press(press_name = '机械工业出版社')
    p2 = Press(press_name = '人民文学出版社')
    p3 = Press(press_name = '新华出版社' )
    p4 = Press(press_name = '人民邮电出版社' )
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()
    bk1 = Book(name='老王回忆录', time='2020-8-29', value=120, number=1)
    bk2 = Book(name='我读书少你别骗我', time='2020-7-29', value=130, number=1)
    bk3 = Book(name='如何征服美丽少女', time='2020-6-29', value=140, number=1)
    bk4 = Book(name='如何征服美丽少男', time='2020-6-29', value=150, number=1)
    bk5 = Book(name='如何使自己变得更骚', time='2020-6-29', value=160, number=1)
    bk6 = Book(name='我变秃了，也变强了', time='2020-6-29', value=170, number=1)
    '''bk1 = Book(name='老王回忆录', time='2020-8-29')
    bk2 = Book(name='我读书少你别骗我', time='2020-7-29')
    bk3 = Book(name='如何征服美丽少女', time='2020-6-29')
    bk4 = Book(name='如何征服美丽少男', time='2020-6-29')
    bk5 = Book(name='如何使自己变得更骚', time='2020-6-29')
    bk6 = Book(name='我变秃了，也变强了', time='2020-6-29')'''
    '''
    bk1 = Book(name='老王回忆录', time = '2020-8-29', value = 120,number = 1,  author_id = au1.id, Category_id = c1.id, Press_id = p1.id, Language_id = l1.id )
    bk2 = Book(name='我读书少你别骗我', time = '2020-7-29', value = 130,number = 1,author_id = au1.id,Category_id = c1.id, Press_id = p1.id, Language_id = l1.id)
    bk3 = Book(name='如何征服美丽少女', time = '2020-6-29', value = 140,number = 1,author_id = au2.id,Category_id = c2.id, Press_id = p2.id, Language_id = l2.id)
    bk4 = Book(name='如何征服美丽少男', time = '2020-6-29', value = 150,number = 1, author_id = au2.id,Category_id = c2.id, Press_id = p2.id, Language_id = l2.id)
    bk5 = Book(name='如何使自己变得更骚', time = '2020-6-29', value = 160,number = 1,author_id = au3.id,Category_id = c3.id, Press_id = p3.id, Language_id = l3.id)
    bk6 = Book(name='我变秃了，也变强了', time = '2020-6-29', value = 170,number = 1,author_id = au3.id,Category_id = c3.id, Press_id = p3.id, Language_id = l3.id)''''''
    #往附表books里插数据，附表的外键 = 主表的主键'''
    db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6])

    db.session.commit()
    #库存
    g1 = Goods( Goods_id = bk1.id)
    g2 = Goods(id = 664, Goods_id = bk2.id)
    g3 = Goods(id = 437, Goods_id = bk3.id)
    g4 = Goods(id = 765, Goods_id = bk4.id)
    g5 = Goods(id = 565, Goods_id = bk5.id)
    g6 = Goods(id = 535, Goods_id = bk6.id)
    g7 = Goods(id = 356, Goods_id = bk6.id)
    g8 = Goods(id = 665, Goods_id = bk5.id)
    g9 = Goods(id = 855, Goods_id = bk5.id)

    db.session.add_all([g1, g2, g3, g4, g5, g6, g7, g8, g9])
    g1 = Goods(id = g1.id)

    db.session.commit()
    app.run(debug = True)