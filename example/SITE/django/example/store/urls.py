from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$'                      , views.index, name='index'),
    url(r'^(?P<id_tovar>\d+)/edit$'  , views.edit, name='edit'),
    # name имя приложения и если указан namespace в глобальном файле urls то оно уникально в пределах этого файла
    url(r'^(?P<id_tovar>\d+)/save$'  , views.save, name='save'),
    url(r'^new$'                     , views.new, name='new'),
    url(r'^(?P<id_tovar>\d+)/delete$', views.delete, name='delete'),

    url(r'^groups/?$', views.group_index, name='group_index'),
    url(r'^groups_new$', views.group_new, name='group_new'),
    url(r'^(?P<id_group>\d+)/groups_edit$', views.group_edit, name='group_edit'),
    url(r'^(?P<id_group>\d+)/groups_delete$', views.group_delete, name='group_delete'),
]