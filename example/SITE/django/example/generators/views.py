from django.shortcuts import render
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO




# Create your views here.
def my_csv(request):
    # при генерации любого контекста отличного от html
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # print('Здесь пишем в файл текст', file=response)

    writer = csv.writer(response)
    for k in range(0, 100):
        writer.writerow([k, k*k, k-2])
    return response

def my_pdf(request):
    response = HttpResponse (content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    p = canvas.Canvas(response)

    p.drawString(100, 500, 'Hello, world!')
    # от точки с координатами писать текст точка отсчета от нижнего левого угла
    p.showPage()
    # переворачиваем страницу
    p.drawString(100, 250, 'Hello, Universe!')
    p.showPage()
    p.save()
    return response

def my_graph(request):

    matplotlib.use('agg')

    X = np.linspace(-10.0, 10.0, 200)
    # создает массив от -10 до 10 раскидаем 200 точек
    Y1 = np.sin(X*X)
    Y2 = np.log(X*X + 0.1)/100.0

    f, ax = plt.subplots()
    ax.plot(X, Y1)
    ax.plot(X, Y2)

    buf = BytesIO()
    f.savefig(buf, format='png')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    return response


