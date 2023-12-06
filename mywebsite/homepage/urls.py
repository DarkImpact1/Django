from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='index.html'),
    path('add/',views.add, name='add'),
    path('multiply/',views.multiply,name='multiply'),
    path('divide/',views.divide,name='divide'),
    path('substract/',views.substract,name='substract')
]
