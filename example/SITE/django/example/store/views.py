from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Tovar

# Create your views here.
def index(request):
    # функция представления
    all_tovars = Tovar.objects.all()
    # name = 'Vasya'
    # # первый шаг собираем данные
    # familia = 'Petrov'
    #
    # # template = loader.get_template('store/index.html')
    # # второй шаг загружаем шаблон указывается относительный путь
    #
    # # context =  {
    # #     'name': name,
    # # }
    # context = locals()
    # # третий шаг формируем контекст
    #
    # response_body = template.render(context)
    # # четвертый шаг формируем тело запроса
    #
    # R = HttpResponse(response_body)
    # # пятый шаг формируется ответ

    R = render(request, 'store/index.html', locals())
    return R

