from django.http import HttpResponse
import datetime
#from django.template import Template
#from django.template.loader import get_template
from django.shortcuts import render

def saludo(request):  #primera vista
    return HttpResponse("Hola alumnos primera pagina en django")

def despedida(request):
    return render(request,"plantillas/misplantillas.html")

def tomarfecha(request):
    fecha_actual=datetime.datetime.now()
    documento='''<html>
    <body>
    <h1>
    fecha y hora actuales %s
    </h1>
    </body>
    </html>'''%fecha_actual
    return HttpResponse(documento)