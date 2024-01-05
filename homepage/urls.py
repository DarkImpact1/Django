from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='index.html'),
    path('email',views.e_mail,name='email'),
    path('show_popup',views.show_popup,name='show_popup')
]

