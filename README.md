# Books_management
## 功能：
此**Books_management**模拟用户操作利用python的**sqlalchemy**包连接mysql数据库存储书籍和用户信息，**matplotlib**绘图函数进行数据分析和统计，用户可先注册，登录系统，进行借书：（borrow），查看图书信息（check），图书入库（add）等操作，账户信息和添加书籍时间，借书时间，借书用户，借出书籍信息，入库书籍信息，入库时间等会被记录，操作完毕后均返回菜单界面，用户可选择退出；查询书籍时，可根据书籍出版社，语言，作者等信息分别统计书籍数量，绘制折线图，借出最频繁的书籍排行前30.数据库初始数据随机生成，其他数据在数据库开启后自行添加。
## 结构：
数据库结构：包含六个表：Author，Goods，Press，Language，Book，Category，Book表为主表，其他各表的id为外键，记录一对多关系，加入主表字段，主表id作为外键成为Goods中的Goods_id列，Goods记录库存量，登录Register表和注册User表初始数据相同，登录表各表id自动升序生成。
