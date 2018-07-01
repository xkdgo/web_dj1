"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^tovar/', include(('store.urls', 'namespace_store'), namespace='namespace_store')),
    # по умолчанию в джанго неймспейс глобальный чтобы разлелять одинаковые имена в разных приложениях
    # добавляется параметр namespace
    url(r'^privet/', include('store.urls')),
    path('admin/', admin.site.urls),
    url(r'^gen/', include(('generators.urls', 'namespace_gen'), namespace='namespace_gen')),
]
