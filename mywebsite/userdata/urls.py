from django.urls import path,include
from . import views


urlpatterns = [
    path('register',views.register, name= "register"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('details',views.user_details,name='userdetails'),
    path('contacts',views.contact_details,name='contactdetails'),
    path('education',views.education_details,name='educationdetails'),
    path('projects',views.project_details,name='projectdetails'),
]
