# 数据模型模块 使用ORM框架
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='TITLE')
    content = models.TextField(null=True)
