from mysql3 import  *
@app.route('/',methods = ['POST','GET'])
#这个url地址允许 POST与GET 请求两种方式,
# 是个列表也就是意味着可以允许多重请求方式，
# 这里表单提交需要通过GET显示HTML页面，再通过POST提交数据
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
            Book(id = a.id)
            db.session.commit()
        if not lan:
            l = Language(
                name = form.language.data
            )
            db.session.add(l)
            Book(id=l.id)
            db.session.commit()
        if not pre:
            p = Press(
            name = form.press.data
            )
            db.session.add(p)
            Book(id=p.id)
            db.session.commit()
        if not cat:
            c = Category(
               name = form.category.data
            )
            db.session.add(c)
            Book(id=c.id)
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
    return render_template('books.html', form = form)
#返回模板渲染