from django.http import HttpResponse
from AppCoder.models import models,Alimentos,Accesorios,Servicios,Contacto
from django.shortcuts import render





def inicio(request):
    
    return render(request, r"C:\Users\MSI GX70\Desktop\MVC-DaianaFernandez-master\Django2\EntregaIntermediaFernandez\AppCoder\templates\index.html")

def alimentos(request):
    menu1 = Alimentos.objects.all()
    return render(request, r"C:\Users\MSI GX70\Desktop\MVC-DaianaFernandez-master\Django2\EntregaIntermediaFernandez\AppCoder\templates\alimentos.html", {"alimentos": menu1})

def accesorios(request):
    menu2= Accesorios.objects.all()
    return render(request, r"C:\Users\MSI GX70\Desktop\MVC-DaianaFernandez-master\Django2\EntregaIntermediaFernandez\AppCoder\templates\accesorios.html", {"accesorios": menu2} )

def servicios(request):
    menu3 = Servicios.objects.all()
    return render(request, r"C:\Users\MSI GX70\Desktop\MVC-DaianaFernandez-master\Django2\EntregaIntermediaFernandez\AppCoder\templates\servicios.html", {"servicios": menu3} )


def contacto(request):
    menu4 = Contacto.objects.all()
    return render(request, r"C:\Users\MSI GX70\Desktop\MVC-DaianaFernandez-master\Django2\EntregaIntermediaFernandez\AppCoder\templates\contacto.html", {"contacto": menu4} )



    

