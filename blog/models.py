# 数据模型模块 使用ORM框架
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='TITLE')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True)
    # 无效
    # def __unicode__(self):
    #     return self.title

    # 有效
    def __str__(self):
        return self.title
