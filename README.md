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
