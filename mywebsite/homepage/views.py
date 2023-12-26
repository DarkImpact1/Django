from django.shortcuts import render
from django.http import HttpResponse
from userdata.models import Projectdetail,Educationdetail,Userdetail
from django.contrib import messages

# Create your views here.

def home(request):
    active_user = request.session.get('active_user',None)
    projects = Projectdetail.objects.filter(username = active_user )
    user_s = Userdetail.objects.filter(username = active_user)
    education = Educationdetail.objects.filter(username = active_user)



    return render(request,'index.html', {'allprojects' : projects})
