from django.shortcuts import render
from django.http import HttpResponse
from .models import Project_Detail
from django.contrib import messages

# Create your views here.

def home(request):
    projects = Project_Detail.objects.all()
    return render(request,'index.html', {'allprojects' : projects})
