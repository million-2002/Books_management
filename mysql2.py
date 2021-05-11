from flask import Flask,render_template,flash,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm#定义表单
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
#数据库配置
app.secret_key = 'csdnblog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wanyanfei123@localhost:3306/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#作者模型
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)#主键
    name = db.Column(db.String(16), unique=True)
    #关系引用
    books = db.relationship('Book', backref='author')
    #反向关联，查询books表，返回books—-obj，
    # books-obj。author找到books外键关联数据
    #查books返回authors
    def __repr__(self):
        return 'Author :%s' % self.name
#书籍模型
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)# 主键
    name = db.Column(db.String(16), unique=True)
    #unique=True表示重复出现的记录只保存一条
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
    authors = db.relationship('Author',backref='author')
    def __repr__(self):
        return 'Book :%s %s' % (self.name, self.author_id)
#传入表单
class Author_form(FlaskForm):
    flash('添加书籍')
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('书名', validators=[DataRequired()])
    bookid = StringField('自定义书号', validators=[DataRequired()])

#validators=[DataRequired()]对于用户提交的数据进行验证，是否为空
#在此对应用户id和书籍id
    submit = SubmitField('提交')
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    author = Author.query.get(author_id)
    #get()，参数为主键，如果主键不存在没有返回内容,返回主键键值对象
    if author:
        try:
            Book.query.filter_by(author_id = author.id).delete()
            #删除某作者和他的书
            #查询Book副键对应的实例，然后删掉
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者失败')
            db.session.rollback()
            #数据库会话回滚，
            # 通过db.session.rollback()方法，
            # 实现会话提交数据前的状态
    else:
        flash('作者没找到')
    return redirect(url_for('index'))
#
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    #查询是否存在该ID的书
    book= Book.query.get(book_id)
    #如果有就删除
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍失败')
            db.session.rollback()
    else:
        #书籍不存在提示错误
        flash('书籍没有找到')
    #url_for传入视图函数名,返回该视图函数对应的路由地址
    #redirect()，功能就是跳转到指定的url
    return redirect(url_for('index'))
@app.route('/',methods = ['POST','GET'])
#这个url地址允许 POST与GET 请求两种方式,
# 是个列表也就是意味着可以允许多重请求方式，
# 这里表单提交需要通过GET显示HTML页面，再通过POST提交数据
def index():
    author_form = Author_form()
    #表单对象author_form
    #调用WTF函数实现验证
    if author_form.validate_on_submit():
        #验证通过获取数据1.查看表单必填数据是否为空：
        # validators=[DataRequired()]，如果不写这句，
        # form.validate_on_submit()就认为表单是空的，所以会false
        author_name = author_form.author.data
        book_name = author_form.book.data

        #判断作者是否存在
        author = Author.query.filter_by(name = author_name).first()
        #如果作者存在
        if author:
            #判断书籍是否存在
            book = Book.query.filter_by(name = book_name).first()
            #有就提示重复
            if book:
                flash('已存在同名书籍')
            #没有重复书籍就添加数据
            else:
                try:
                    new_book = Book(name=book_name,author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()
        #如果作者不存在添加作者书籍
        else:
            try:
                new_author = Author(name = author_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name = book_name,author_id = new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash('添加作者和书籍失败')
                db.session.rollback()
    #验证不通过就提示错误
    else:
        if request.method == 'POST':
            flash('参数不全')
    authors = Author.query.all()#返回查询到的所有对象
    return render_template('books.html', authors=authors, form = author_form)
#返回模板渲染
if __name__ == '__main__':
    db.drop_all() # 删除表
    db.create_all() # 创建表
    #往Author表里插数据
    au1 = Author(name='老王', id = 1111)
    au2 = Author(name='老宋', id = 2222)
    au3 = Author(name='老刘', id = 3333)
    db.session.add_all([au1, au2, au3])
    db.session.commit()
    bk1 = Book(name='老王回忆录',id = 0000, author_id = au1.id)
    bk2 = Book(name='我读书少你别骗我', id = 2000,author_id = au1.id)
    bk3 = Book(name='如何征服美丽少女', id = 4000,author_id = au2.id)
    bk4 = Book(name='如何征服美丽少男', id = 3000, author_id = au2.id)
    bk5 = Book(name='如何使自己变得更骚', id = 5000,author_id = au3.id)
    bk6 = Book(name='我变秃了，也变强了', id = 6000,author_id = au3.id)
    #往附表books里插数据，附表的外键 = 主表的主键
    db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6])
    db.session.commit()
    app.run(debug=True)
