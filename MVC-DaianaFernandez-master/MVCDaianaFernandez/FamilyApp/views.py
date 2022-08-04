from contextvars import Context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template
from FamilyApp.models import Familia


def familia(request):
    return HttpResponse("Bienvenidos a mi registro Familiar")

def familia1(request):

    familia2 = Familia.objects.all()
    
    return render(request, "familia.html",{"familia": familia2},) 