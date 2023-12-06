from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    name = ['Mohit','Dark Impact','ezz_programming']
    return render(request,'index.html', {'name' : name[random.randint(0,2)]})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+ val2
    return render(request, 'result.html', {'answer': res,'number1': val1,'number2': val2,'operator':'+'})

def multiply(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 * val2
    return render(request, 'result.html', {'answer': res,'number1': val1,'number2': val2,'operator':'*'})
    
def substract(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 - val2
    return render(request, 'result.html', {'answer': res,'number1': val1,'number2': val2,'operator':'-'})

def divide(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 / val2
    return render(request, 'result.html', {'answer': res,'number1': val1,'number2': val2,'operator':'/'})