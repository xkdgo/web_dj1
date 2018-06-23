from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .models import Tovar
from datetime import datetime

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

def edit(request, id_tovar):
    try:
        tovar = Tovar.objects.get(pk=id_tovar)
    except Tovar.DoesNotExist as Exc:
        raise Http404('Товар не найден') from Exc
    # return HttpResponse('edit {0}'.format(id_tovar))
    return render(request, 'store/edit.html', locals())

def save(request, id_tovar):
    if request.method.upper() != 'POST':
        raise Http404('Неверный метод запроса')
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    tovar.title = request.POST['title']
    tovar.article = request.POST['article']
    tovar.count = int(request.POST['count'])
    tovar.save()
    return HttpResponseRedirect(reverse('namespace_store:index'))
    # return HttpResponse('save {0}'.format(id_tovar))

def new(request):
    tovar = Tovar()
    tovar.title = '?'
    tovar.article = '?'
    tovar.count = 0
    tovar.arrived = datetime.today()
    tovar.save()
    return HttpResponseRedirect(reverse('namespace_store:edit', args=(tovar.id,)))

def delete(request, id_tovar):
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    tovar.delete()
    return HttpResponseRedirect(reverse('namespace_store:index'))

