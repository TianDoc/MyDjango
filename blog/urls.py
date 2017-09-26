# URL配置文件
# Django项目中所有地址（页面）都需要我们自己去配置其URL
# 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page')
]
