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


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        # 创建成功返回主页
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles}, {'Hello': 'Hello Blog!'})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})