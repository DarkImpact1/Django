from django.db import models
# Create your models here.

class Userdetail(models.Model):
    username = models.CharField(max_length = 50, default = "default")
    full_name = models.CharField(max_length = 50)
    e_mail = models.CharField(max_length = 40 )
    skills = models.CharField(max_length = 250)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='ImagesForHomepage')
    carrer_goal = models.CharField(max_length = 50)

    class Meta:
        app_label = 'userdata'

class Educationdetail(models.Model):
    username = models.CharField(max_length = 50, default = "default")
    college_name = models.CharField(max_length = 250)
    degree_name = models.CharField(max_length = 50)
    college_start_year = models.CharField(max_length = 40 )
    college_end_year = models.CharField(max_length = 40 )
    about_college = models.TextField()

    xii_school_name = models.CharField(max_length = 250)
    xii_school_board_name = models.CharField(max_length = 50)
    xii_school_start = models.CharField(max_length = 40 )
    xii_school_end = models.CharField(max_length = 40 )
    about_xii_school = models.TextField()

    x_school_name = models.CharField(max_length = 250)
    x_school_board_name = models.CharField(max_length = 50)
    x_school_start = models.CharField(max_length = 40 )
    x_school_end = models.CharField(max_length = 40 )
    about_x_school = models.TextField()


class Projectdetail(models.Model):
    username = models.CharField(max_length = 50, default = "default")
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ImagesForHomepage')
    htmlid = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=20)
    link = models.URLField()