from mysql3 import *
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
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    #查询是否存在该ID的书
    category= Category.query.get(category_id)
    #如果有就删除
    if category:
        try:
            db.session.delete(category)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除类别失败')
            db.session.rollback()
    else:
        #书籍不存在提示错误
        flash('类别没有找到')
    #url_for传入视图函数名,返回该视图函数对应的路由地址
    #redirect()，功能就是跳转到指定的url
    return redirect(url_for('index'))
@app.route('/delete_press/<press_id>')
def delete_press(press_id):
    #查询是否存在该ID的书
    press= Press.query.get(press_id)
    #如果有就删除
    if press:
        try:
            db.session.delete(press)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除出版社失败')
            db.session.rollback()
    else:
        #书籍不存在提示错误
        flash('出版社没有找到')
    #url_for传入视图函数名,返回该视图函数对应的路由地址
    #redirect()，功能就是跳转到指定的url
    return redirect(url_for('index'))
@app.route('/delete_language/<language_id>')
def delete_language(language_id):
    #查询是否存在该ID的书
    language = Language.query.get(language_id)
    #如果有就删除
    if language:
        try:
            db.session.delete(language)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除语言失败')
            db.session.rollback()
    else:
        #书籍不存在提示错误
        flash('语言没有找到')
    # url_for传入视图函数名,返回该视图函数对应的路由地址
    # redirect()，功能就是跳转到指定的url
    return redirect(url_for('index'))
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # 查询是否存在该ID的书
    book = Book.query.get(book_id)
    # 如果有就删除
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

