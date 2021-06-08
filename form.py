#from mysql3 import  *
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired
class SigninForm(FlaskForm):
    username = StringField('姓名',validators=[DataRequired()])
    password = IntegerField('密码', validators=[DataRequired()])
    submit1 = SubmitField('注册')
class RegisterForm(FlaskForm):
    username = StringField('姓名', validators=[DataRequired()])
    password = IntegerField('密码', validators=[DataRequired()])
    submit2 = SubmitField('登录')
class Aform(FlaskForm):
    #flash('添加书籍')
    book = StringField('书名', validators=[DataRequired()])
    press_time = StringField('出版时间')
    value = IntegerField('价格', validators=[DataRequired()])
    num = IntegerField('数量', validators=[DataRequired()])
    author_name = StringField('作者', validators=[DataRequired()])
# bookid = StringField('自定义书号', validators=[DataRequired()])
    language = StringField('语言', validators=[DataRequired()])
    press = StringField('出版社', validators=[DataRequired()])
    category = StringField('类别', validators=[DataRequired()])
# validators=[DataRequired()]对于用户提交的数据进行验证，是否为空
# 在此对应用户id和书籍id
    submit = SubmitField('提交')