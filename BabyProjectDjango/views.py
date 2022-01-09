from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    hell = 'Hello World!'

    '''Указываем параметры подачи в шаблон с помощью словаря'''
    return render(request, './index.html', {
        'hell':hell
    })