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



