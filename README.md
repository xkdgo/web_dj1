#python3-pip install django
#sudo python3 -m pip install psycopg2-binary
# sudo python3 -m pip install psycopg2==2.7.1
# sudo python3 -m pip install --upgrade psycopg2==2.7.1
# sudo python3 -m pip install --upgrade psycopg2
# sudo python3 -m pip install --upgrade --ignore-installed psycopg2
# sudo apt-get install nginx




# web_dj1
Django project 1

dbcreate:

linux_user@pc_name:~$ sudo su postgres

[sudo] пароль для linux_user:

postgres@pc_name:/home/linux_user$ psql

psql (9.5.13)
Type "help" for help.

postgres=# create user dbuser with password 'dbpassword';
CREATE ROLE

postgres=# create database example with owner dbuser;
CREATE DATABASE

postgres=# \q

postgres@pc_name:/home/linux_user$ exit
linux_user@pc_name:~$

#django install
linux_user@pc_name:~$ python3 -m pip install django


#django create
linux_user@pc_name:~/PycharmProjects/web_dj1/example/SITE/django$ ls
linux_user@pc_name:~/PycharmProjects/web_dj1/example/SITE/django$ django-admin startproject example
linux_user@pc_name:~/PycharmProjects/web_dj1/example/SITE/django$ ls
example
linux_user@pc_name:~/PycharmProjects/web_dj1/example/SITE/django$ 


linux_user@pc_name:~/PycharmProjects/web_dj1/example/SITE/django/example$ python3 manage.py runserver

прописываются в settings.py настройки для БД

python3 manage.py migrate
python3 manage.py createsuperuser --username admin

# добавляем новое приложение
python3 manage.py startapp store

# правим models
# правим example/settings.py в части INSTALLED_APPS
# создаем скрипт миграции
python3 manage.py makemigrations store
# смотрим какие правки в БД внесутся
python3 manage.py sqlmigrate store 0001
# применяем настройки
python3 manage.py migrate

добавляются в urls.py ссылка на store

sudo apt-get install libapache2-mod-wsgi-py3

Настройка nginx в связке с django
sudo python3 -m pip install uwsgi
http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#nginx-and-uwsgi-and-test-py


uwsgi --socket example.sock --module example.wsgi --chmod-socket=666 --env DJANGO_SETTINGS_MODULE=example.settings --chdir ~/PycharmProjects/web_dj1/example/SITE/django/example

Правится settings.py в части static
# указывает на папку example/SITE/htdocs/static
# в nginx или apache2 указывается alias на абсолютный путь
# после этого запускаем
python3 manage.py collectstatic

store/urls.py и store/views.py в части обработки request-ов

# Добавляем класс Tovar в админку
правка store/admin.py

# для корректного отображения названий класса Tovar в админке
# добавляется метод __str__ в классе Tovar файл store/models.py

# создали шаблон в store/templates/store
index.html

# в файле store/views.py подправили функцию для отображения списка товаров

# в шаблоне записали обработчик получаемого словаря locals() из функции index

# добавили функцию edit сделали табличку в темплейте index.html
# в глобальном файле urls ввели понятие namespace_store
# описываем его в темплейте как ссылка на функцию  namespace_store:edit

# в темплейте edit делается action с ссылкой на функцию save (namespace_store:save)
# описывается функция save в файле store/views.py

# в store.urls добавляем url new и delete - где сопоставляется ссылка url namespace_store:xxx
# и функции views.xxx
# в темплейте index делается  с ссылкой  a href на функцию new (namespace_store:new)
# описывается функция new в файле store/views.py

# в темплейте index делается  с ссылкой  a href на функцию delete (namespace_store:delete)
# описывается функция delete в файле store/views.py


# models.py переделываем в модуль models
# models.py переименовываем в Tovar.py и помещаем в models
# в models/__init.py__ делаем соответствующий импорт

# создаются доп модели Group и Tag в файле models/Group.py
# выполняется шаг миграции

#migrations for Group and Tag:

#python3 manage.py makemigrations
Migrations for 'store':
  store/migrations/0002_group_tag.py
    - Create model Group
    - Create model Tag


# файл store/migrations/0002_group_tag.py обязательно просматривается глазами

# После этого делается команда

python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, store
Running migrations:
  Applying store.0002_group_tag... OK


# В файле store/admin.py регистрируем модели

# Через админ-панель добавляются записи в БД

# создаем связи в модели Tovar на Group и Tag (ForeignKey и ManyToManyField)

# Шаг makemigrations
python3 manage.py makemigrations
Migrations for 'store':
  store/migrations/0003_auto_20180626_1927.py
    - Add field group to tovar
    - Add field tags to tovar


# смотрим файл миграции глазами

# применяем миграцию

python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, store
Running migrations:
  Applying store.0003_auto_20180626_1927... OK

# создаем аналогичные представления для groups
# правится файл urls.py
    url(r'^groups$', views.group_index, name='group_index'),
    url(r'^groups_new$', views.group_new, name='group_new'),
    url(r'^(?P<id_group>\d+)/groups_edit$', views.group_edit, name='group_edit'),
    url(r'^(?P<id_group>\d+)/groups_delete$', views.group_delete, name='group_delete'),
# правится файл views.py
   описываются соответствующие функции
   views.group_index, views.group_new, views.group_edit, views.group_delete
# создается файл store/templates/store/group_index.html
   с необходимыми ссылками на нужные url

# Создаем пакет store/forms
# в нем описывается файл Group.py

# В проекте создается вспомогательный пакет helpers
# сюда будут складываться вспомогательные функции
# создается вспомогательный класс restful который будет использоваться как декоратор

# в store/views создается две функции group_edit
# одна для метода GET другая для метода POST - реализуется что-то на подобие мультиметода с использованием
# restful как декоратора для функции store/views/group_edit
# функция передает параметры в шаблон store/group_edit.html

# для отображения и запуска функций создается шаблон store/template/store/group_edit.html
# в этом шаблоне принимаются параметры в виде {{ form }}

# примеры с формами закончены и для фиксации как это работает переименовываются
# store/views.py -> store/views.py.bak.001
# store/forms/Group.py -> store/forms/Group.py.bak

# Теперь рассматриваем форму модели
# в файле store/forms/Group создается Meta класс
# store/views.py правятся функции group_edit


# 5
# sudo apt-get install texlive
# python3 -m pip install reportlab

# python3 manage.py startapp generators
# делаем функцию generators/views/ my_csv
# регистрируем приложение в settings.py
# INSTALLED_APPS добавляем 'generators'

# в urls.py добавляем ссылку на generators
# url(r'^gen/', include(('generators.urls', 'namespace_gen'), namespace='namespace_gen')),

# в файле generators/urls.py создаем ссылку на my_csv из generators/views

# то же самое для генерации pdf

# 5.2

# sudo python3 -m pip install matplotlib
# sudo apt-get install python3-tk возможно этот пакет не нужен

# то же самое для генерации png рисунка








