from django.shortcuts import render
from .models import Order


def first_page(request):
    object_list = Order.objects.all()

    '''Указываем параметры подачи в шаблон с помощью словаря'''
    return render(request, './index.html', {'object_list':object_list})