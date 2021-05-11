from mysql3 import  *
class Aform(FlaskForm):
    #flash('添加书籍')
    book = StringField('书名', validators=[DataRequired()])
    press_time = StringField('出版时间')
    value = IntegerField('价格', validators=[DataRequired()])
    num = IntegerField('数量', validators=[DataRequired()])
    author_name = StringField('作者', validators=[DataRequired()])
#  bookid = StringField('自定义书号', validators=[DataRequired()])
    language = StringField('语言', validators=[DataRequired()])
    press = StringField('出版社', validators=[DataRequired()])
    category = StringField('类别', validators=[DataRequired()])
#validators=[DataRequired()]对于用户提交的数据进行验证，是否为空
#在此对应用户id和书籍id
    submit = SubmitField('提交')