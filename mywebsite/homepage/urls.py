from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='index.html'),
    path('email',views.e_mail,name='email')
]

