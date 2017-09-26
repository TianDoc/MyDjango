# MyDjango
Django python WEB开发项目

## Django入门与实践
* http://www.imooc.com/learn/790

## Template
* 步骤：
  1. 在APP中的根目录下创建叫templates
  2. 在该目录下创建HTML文件
  3. 在view.py中返回render()

* DTL的使用
  1. render()函数中支持一个dict类型参数
  2. 该字典是后台传递到模板的参数，键为参数名
  3. 在模板中使用{{参数名}}来直接使用

* 注意点：
  1. Django查找Template <br>
     Django按照INSTALLED_APPS中的添加顺序查找Templates
  2. 不同APP下Template目录中的同名.html文件会造成冲突
  3. 解决Templates冲突方案：<br>
     在APP的Template目录下创建以APP名为名称的目录

## Models
* Modles
  1. 一个Modles对应的数据库的一张表
  2. Django中Modles以类的形式表现
  3. 包含了一些基本字段和数据行为

* ORM对象关系映射
  1. 实现了对象和数据库之间的映射
  2. 隐藏了数据访问细节，不需要编写SQL语句

* 编写Modles步骤：
  1. 在应用的根目录下创建models.py,并引入models模块
  2. 创建类，继承models.Model,该类是一张数据表
  3. 在类中创建字段

* 字段创建
  1. 字段即类里面的属性（变量）
  2. attr(变量) = models.CharField(max_length=64)

* 生成数据表
  1. 命令行进入manage.py同级目录
  2. 执行 python manage.py makemigrations app名（可选）
  3. 再执行python manage.py migrate

* 查看
  1. Django会自动在app/migrations/目录下生成移植文件
  2. 执行python manage.py sqlmigrate 应用名 文件id查看SQL语句
  3. 默认sqlite3的数据库在项目根目录下db.sqlite3

* 后台步骤：
  1. views.py中import models
  2. article = models.Article.objects.get(pk=1) id等于1
  3. render(request,page,{'article',article})

* 前端步骤：
  1. 模板可直接使用对象及对象的"."操作
  2. {{article.title}}

## Admin
* Admin
  1. Admin是Django自带的一个功能强大的自动化数据管理界面
  2. 被授权的用户可直接在Admin中管理数据库
  3. Django提供了许多针对Admin的定制功能

* 配置Admin

* 创建用户
  1. python manage.py createsuperuser创建超级用户
  2. localhost:8000/admin/ Admin入口
  3. 汉化 修改settings.py中LANGUAGE_CODE= 'zh_Hans'

* 配置应用
  1. 在应用下admin.py中引入自身的models模块（或里面的模型类）
  2. 编辑admin.py: admin.site.register(models.Article)

* 修改数据
  1. 点击Article超链接进入Article列表页面

* 修改数据默认名车
  1. 在Article类下添加一个方法
  2. 根据Python版本选择_str_(self)或_unicode_(self)
  3. return self.title

* 页面for循环： <br>

        {% for xx in xxs %}
        HTML语句
        {% endfor %}


* URL传递参数：
  1. 参数写在响应函数中request后，可以有默认值
  2. URL正则表达式：r'^article/(?P<article_id>[0-9]+)/$'
  3. URL正则中的组名必须和参数名一致

* Template超链接配置
  1. template中可以用"{%url 'app_name:url_name' param%}"
  2. 其中app_name 和 url_name 都在url中配置的

* url函数的名称参数
  1. 根urls,写在include()的第二个参数位置，namespace = 'blog'
  2. 应用下则写在url()的第三个参数位置， name= 'article'
  3. 主要取决于是否使用了include引用了另一个url配置文件





