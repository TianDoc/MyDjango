from django.contrib import admin

from blog.models import Article


# Register your models here.
# 该应用的后台管理系统的配置文件

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Article, ArticleAdmin)
