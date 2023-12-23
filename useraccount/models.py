from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userdetail(models.Model):
    
    full_name = models.CharField(max_length = 50)
    e_mail = models.CharField(max_length = 40 )
    skills = models.CharField(max_length = 250)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='ImagesForHomepage')
    carrer_goal = models.CharField(max_length = 50)

    class Meta:
        app_label = 'useraccount'