from django.db import models

# Create your models here.
# well this is simple class, it won't work in database to in order to convert your class to 
# table just inherit the property from model and remember str, int is not a field in database 
# so you have to also convert in 


class Project_Detail(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ImagesForHomepage')
    htmlid = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=20)
    link = models.URLField()


    class Meta:
        app_label = 'homepage'
