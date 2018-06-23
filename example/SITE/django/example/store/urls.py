from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$'                      , views.index, name='index'),
    url(r'(?P<id_tovar>\d+)/edit'  , views.edit, name='edit'),
    # name имя приложения и если указан namespace в глобальном файле urls то оно уникально в пределах этого файла
    url(r'(?P<id_tovar>\d+)/save'  , views.save, name='save'),
    url(r'new'                     , views.new, name='new'),
    url(r'(?P<id_tovar>\d+)/delete', views.delete, name='delete'),

]