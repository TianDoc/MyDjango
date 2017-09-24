# from django.http import HttpResponse
from django.shortcuts import render


# 1. 在先前创建的 HelloWorld 目录下的 HelloWorld 目录新建一个 view.py 文件
# def hello(request):
#     return HttpResponse("Hello world ! ")



# 使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数。
# context 字典中元素的键值 "hello" 对应了模板中的变量 "{{ hello }}"。
def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)
