from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from  flask import Flask,config#config包存放配置文件

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:wanyanfei123@localhost:3306/library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
'''SQLAlchemy是一个关系型数据库框架，
它提供了高层的 ORM 和底层的原生数据库的操作，
让开发者不用直接和 SQL 语句打交道，而是通过 Python 对象来操作数据库，
在舍弃一些性能开销的同时，换来的是开发效率的较大提升'''
if __name__ == '__main__':
     # 迁移数据库
     db.create_all()

class User(db.Model):
    __tablename__ = 'user_list' #（设置表名）
    id = db.Column(db.Integer, primary_key=True) #（设置主键）
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    #每个Column表示数据库中的一列
    def __repr__(self):
        return '<User 用户名：%r 密码：%r>' % (self.username, self.password)

def add_object(user):
        db.session.add(user)
        db.session.commit()
        print("添加 % r 完成" % user.__repr__)
user = User()

user.username = '占三'
user.password = '123456'
add_object(user)
'''
def query_object(user, query_condition_u, query_condition_p):
    result = user.query.filter(and_(user.username == query_condition_u, user.password == query_condition_p))
    print("查询 % r 完成" % user.__repr__)
    return result
def delete_object(user):
    result = user.query.filter(user.username == '11111').all()
    db.session.delete(result)
    db.session.commit()
#改
def update_object(user):
    result = user.query.filter(user.username == '111111').all()
    result.title = 'success2018'
#db.create_all()'''