from django.contrib import admin
from .models import Userdetail,Projectdetail,Educationdetail,WorkDetail,Servicedetails,Contactdetail
# Register your models here.
admin.register(Userdetail)
admin.register(Projectdetail,Educationdetail,WorkDetail,Servicedetails,Contactdetail)