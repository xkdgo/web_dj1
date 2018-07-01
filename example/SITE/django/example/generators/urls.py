from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^csv/?$', views.my_csv, name='my_csv'),
    url(r'^pdf/?$', views.my_pdf, name='my_pdf'),
    url(r'^img/?$', views.my_graph, name='my_graph'),
]