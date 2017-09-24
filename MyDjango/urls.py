"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
# 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from . import view

# urlpatterns = [
#     url(r'^$', view.hello),
# ]

urlpatterns = [
    # url() 函数
    # Django url() 可以接收四个参数，
    # 分别是两个必选参数：regex、view 和
    # 两个可选参数：kwargs、name，接下来详细介绍这四个参数。
    # regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
    # view: 用于执行与正则表达式匹配的 URL 请求。
    # kwargs: 视图使用的字典类型的参数。
    # name: 用来反向获取 URL。
    url(r'^hello$', view.hello),
]
