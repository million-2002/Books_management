from flask import Flask,render_template,flash,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
#定义表单
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired
app = Flask(__name__)
#数据库配置
app.secret_key = 'csdnblog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wanyanfei123@localhost:3306/library2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)






