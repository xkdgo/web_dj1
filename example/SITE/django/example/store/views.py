from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # функция представления
    time = datetime.now()
    presentation = 'Hello, World <br/><br/>{}'.format(time)
    R = HttpResponse(presentation)
    return R

