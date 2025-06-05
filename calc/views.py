from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def calculadora(request):
    resultado = None
    num1 = int(request.POST.get('num1', 0))
    num2 = int(request.POST.get('num2', 0))
    operacion = request.POST.get('operacion')

    if operacion == 'sumar':
        resultado = num1 + num2
        
    elif operacion == 'resta':
        resultado = num1 - num2

    return render(request, 'base.html', {"resultado": resultado})
