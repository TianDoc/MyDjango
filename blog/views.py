from django.shortcuts import render

from . import models


# Create your views here.
# def index(request):
#     return HttpResponse('Hello World Blog')

def index(request):
    # {'Hello': 'Hello Blog!'}, all() 获取文章的全部对象 返回的就是一个列表
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles}, {'Hello': 'Hello Blog!'})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
