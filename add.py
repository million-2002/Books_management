from form import  *
from library import  *
#这个url地址允许 POST与GET 请求两种方式,
# 是个列表也就是意味着可以允许多重请求方式，
# 这里表单提交需要通过GET显示HTML页面，再通过POST提交数据
@app.route('/multi-form', methods=['POST'])
def multi_form():
    signin_form = SigninForm()
    register_form = RegisterForm()
    #validate()逐个对字段调用字段实例化时定义的验证器，返回表示验证结果的布尔值
    if signin_form.submit1.data and signin_form.validate():
        username = (signin_form.username.data,
                    signin_form.password.data)
        db.session.add(username)
        User(id = username.id)
        db.session.commit()
        flash('%s, you just submit the Signin Form.' % username)
        return redirect(url_for('index'))

    if register_form.submit2.data and register_form.validate():
        #username = register_form.username.data
        username = (register_form.username.data,
                    register_form.password.data)
        db.session.add(username)
        Register(id = username.id)
        db.session.commit()
        flash('%s, you just submit the Register Form.' % username)
        return redirect(url_for('index'))
    return render_template('2form.html', signin_form = signin_form,register_form = register_form)

@app.route('/',methods = ['POST','GET'])
def index():
    form = Aform()
    #表单对象author_form
    #调用WTF函数实现验证
    if form.validate_on_submit():
        #验证通过获取数据1.查看表单必填数据是否为空：
        # validators=[DataRequired()]，如果不写这句，
        # form.validate_on_submit()就认为表单是空的，所以会True
        aut = Author.query.filter_by(author_name = form.author_name.data).first()
        lan = Language.query.filter_by(language_name = form.language.data).first()
        pre = Press.query.filter_by(press_name = form.press.data).first()
        cat = Category.query.filter_by(category_name = form.category.data).first()
        if not aut:
            a = Author(
                name = form.author_name.data
            )
            db.session.add(a)
            Author(id = a.id)
            db.session.commit()
        if not lan:
            l = Language(
                name = form.language.data
            )
            db.session.add(l)
            Language(id=l.id)
            db.session.commit()
        if not pre:
            p = Press(
            name = form.press.data
            )
            db.session.add(p)
            Press(id=p.id)
            db.session.commit()
        if not cat:
            c = Category(
               name = form.category.data
            )
            db.session.add(c)
            Category(id=c.id)
            db.session.commit()
        #if aut and lan and pre and cat:
        newform = Book(
                            name = form.book.data,
                            time = form.press_time.data,
                            value = form.value.data,
                            number = form.num.data,
                            #author_id = aut.id,
                            #Category_id = cat.id,
                            #Press_id = pre.id,
                            #Language_id = lan.id
                        )
        db.session.add(newform)
        Book(id = newform.id)
        db.session.commit()

        goods = Goods(
                Goods_id = newform.id
            )
        db.session.add(newform)
        Book(id = goods.id)
        db.session.commit()
    return render_template('form.html', form = form)
# 这是一个不存在的渲染。。
#返回模板渲染