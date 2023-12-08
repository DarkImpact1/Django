from django.db import models

# Create your models here.
class Person_Detail:
    full_name = str
    aim = str
    introduction = str

class Education_Detail:
    college_details = str
    senior_secondary_detail = str
    metriculation_detail = str

class Project_Detail:
    name = str
    image = str
    id = str
    href = str
    description = str
    category = str
    link = str

class Service_Detail:
    service_name = str
    service_detail = str

class Contact_Detail:
    contact_number = str
    whatsapp_number = str
    email = str
    linkedin_link = str
    instagram_link =str
    facebook_link = str
    twitter_link = str
