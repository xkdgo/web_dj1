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

http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#nginx-and-uwsgi-and-test-py

uwsgi --socket example.sock --module example.wsgi-chmod-socket=666 --env DJANGO_SETTINGS_MODULE=example.settings --chdir ~/PycharmProjects/web_dj1/example/SITE/django/example

