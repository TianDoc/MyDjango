from django.shortcuts import render

from . import models

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World Blog')

def index(request):
    article = models.Article.objects.get(pk=1)  # {'Hello': 'Hello Blog!'},
    return render(request, 'index.html', {'article': article}, {'Hello': 'Hello Blog!'})
