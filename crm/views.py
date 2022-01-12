from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


def first_page(request):
    slider_list = CmsSlider.objects.all() #get all objects from db
    '''Указываем параметры подачи в шаблон с помощью словаря'''
    return render(request, './index.html', {'slider_list': slider_list})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()

    return render(request, './thanks_page.html', {'name': name, 'phone': phone})
