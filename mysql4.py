# coding=utf-8
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
"""
1. 配置数据库
    a.导入SQLALchemy扩展
    b.创建db对象, 并配置参数
    c.终端创建数据库
2. 添加作者和书模型(类)
    a.模型继承自db.Model
    b.__tablename__:表名
    c. db.Column:字段
    d. db.relationship:关系引用
3. 添加数据
4. 使用模板显示数据库查询到的数据
    a.查询所有的作者信息, 让信息传递给模板
    b.模板中按照格式, 依次for循环作者和书籍即可(通过作者获取书籍, 用的是关系引用)
5. 使用WTF显示表单 
    a.自定义表单类
    b.模板中显示
    c.设置secret_key
6. 实现相关的增删逻辑
    a.添加作者/书籍
    b.删除书籍: redirect(重定向)/url_for(指向路由)/for else  的使用.
    c.删除作者(要先删除该作者的书籍, 再删除该作者)
"""
# 配置数据库的地址URI , 格式 "数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名"  , 端口号可以不写.
# python3中用的mysql驱动是mysql-connector , 已经不支持python2的MySQLdb驱动.
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:wanyanfei123@localhost:3306/library1"
# 跟踪数据库的修改 --> 不建议开启 , 一是消耗性能 , 二是未来的版本中会移除.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hwhefsewljfejrlesjfl"      # 没设置secret_key会有报错提醒
# 将app作为参数传入这个关联工具 , 创建一个两者相关联对象db
db = SQLAlchemy(app)

# 注意: web框架里面的模型类基本都是要继承自导入的模块中的某个父类 , 这样才会起到关联的作用.
class Author(db.Model):
    """创建作者子类"""
    __tablename__ = "authors"           # 定义表名
    # 定义字段
    # db.Column表示是一个字段 , db.Integer就代表id这个字段的数据类型是整数 , primary_key代表主键(主关键字) , 是作为表的行的唯一标识.
    # db.String代表是字符串类型 , 字符串长度定义个n个字节 , unique(唯一的) , unique=True代表这列不允许出现重复的值.
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)        # string的长度随便写个2的倍数就行了
    # 在"一对多"的一中定义author_book属性 , 该属性不会出现在字段中 , 后面的backref="author"是给Book反向引用的
    # 由于是"一对多" , 所以"多"的地方用Book参数 , "一"的地方用不加s的实例对象参数author.
    author_book = db.relationship("Book",backref="author")
    def __repr__(self):
        """返回定制消息, 与__str__作用类似"""
        return "Author: %d %s"%(self.id,self.name)

class Book(db.Model):
    """创建书籍子类"""
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey("authors.id"))      # 表名.id 来建立外键关联
    def __repr__(self):
        return "Book: %d %s"%(self.id,self.name)

class TrueForm(FlaskForm):
    """表单扩展常用的模型(类)有三种: StringField, PasswordField,  SubmitField , 这里只用到两种
        然后传入参数并创建出各自的实例对象 , 以供其它地方使用.
    """
    author = StringField("作者",validators=[DataRequired()])
    book = StringField("书籍",validators=[DataRequired()])
    submit = SubmitField("添加")

def make_author_book():
    author1 = Author(name="金庸")
    author2 = Author(name="古龙")
    author3 = Author(name="鲁迅")
    author4 = Author(name="巴金")
    db.session.add_all([author1,author2,author3,author4])
    db.session.commit()
    book1 = Book(name="<<射雕英雄传>>", author_id=author1.id)
    book2 = Book(name="<<天龙八部>>", author_id=author1.id)
    book3 = Book(name="<<鹿鼎记>>", author_id=author1.id)
    book4 = Book(name="<<笑傲江湖>>", author_id=author1.id)
    book5 = Book(name="<<武林外史>>", author_id=author2.id)
    book6 = Book(name="<<萧十一郎>>", author_id=author2.id)
    book7 = Book(name="<<小李飞刀>>", author_id=author2.id)
    book8 = Book(name="<<狂人日记>>", author_id=author3.id)
    book9 = Book(name="<<阿Q正传>>", author_id=author3.id)
    book10 = Book(name="<<家>>", author_id=author4.id)
    book11 = Book(name="<<春>>", author_id=author4.id)
    book12 = Book(name="<<秋>>", author_id=author4.id)
    db.session.add_all([book1,book2,book3,book4,book5,book6,
                        book7,book8,book9,book10,book11,book12])
    db.session.commit()

@app.route("/",methods=["GET","POST"])
def add_author_book():
    true_form = TrueForm()
    """
    1.调用WTF的函数实现验证
    2.验证通过则获取数据
        3.判断作者是否存在
        4.如果作者存在, 则判断书籍是否存在, 没有重复的书籍就添加数据, 如果重复就提示错误.
        5.如果作者不存在, 就添加作者和书籍
    6.验证不通过就提示错误.
    """
    # 调用WTF的函数实现验证
    if true_form.validate_on_submit():
        # 2.验证通过则获取此时填入的数据
        author_name = true_form.author.data
        book_name = true_form.book.data
        # 3.判断作者是否存在, Author.query.filter_by(name=author_name)是查询, .first()才是拿到数据.
        author_query = Author.query.filter_by(name=author_name).first()
        # 4.如果作者存在
        if author_query:
            book_query = Book.query.filter_by(name=book_name).first()       # 查询并拿数据
            if book_query:
                flash("您要添加的书籍已存在!")
            else:
                try:
                    new_book = Book(name="<<%s>>"%book_name,author_id=author_query.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash("添加书籍错误!")
                    db.session.rollback()      # 回滚操作
        else:
            # 5.如果作者不存在
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name="<<%s>>"%book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                flash("添加作者和书籍错误!")
                db.session.rollback()
    else:
        # 验证不通过
        if request.method == "POST":
            flash("参数错误!")
    # 查询所有的作者信息, 让信息传递给模板
    all_authors = Author.query.all()
    return render_template("book_manage.html",all_authors=all_authors,form=true_form)

# 网页中删除书籍-->将book_id参数传到路由, 路由再将book_id传入delete_book函数内部使用.
# < >尖括号代表路由参数, 路由需要接受参数
@app.route("/delete_book/<book_id>",methods=["GET","POST"])
def delete_book(book_id):
    # 1.查询书籍并拿数据
    book = Book.query.get(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        flash("删除错误!")
        db.session.rollback()
    # redirect重定向回到根路径, redirect接收路由地址参数, 或者直接接收网址参数(http://xxxxx.com)
    # url_for("index"): 需要传入视图函数名, 返回该视图函数对应的路由地址(url)
    return redirect(url_for("add_author_book"))

# 删除作者
@app.route("/delete_author/<author_id>",methods=["GET","POST"])
def delete_author(author_id):
    # 1.查询作者并拿数据
    author = Author.query.get(author_id)
    try:
        # 查询书籍并删除, 直接在查询后面跟 .delete()就可以直接将查询到的结果删除掉
        Book.query.filter_by(author_id=author.id).delete()
        db.session.delete(author)
        db.session.commit()
    except Exception as e:
        flash("删除错误!")
        db.session.rollback()        # 回滚
    return redirect(url_for("add_author_book"))       # 重定向回到根路径


if __name__ == '__main__':
    # 先删除所有表, 在创建表之前要先删掉表
    db.drop_all()
    # 再创建所有表
    db.create_all()
    make_author_book()
    app.run(debug=True)