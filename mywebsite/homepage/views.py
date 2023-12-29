from django.shortcuts import render,redirect
from django.http import HttpResponse
from userdata.models import Educationdetail,Userdetail,Contactdetail,Projectdetail,WorkDetail,Servicedetails
from django.contrib import messages

# Create your views here.

def home(request):
    if request.session.get('active_user',None):

        skills =[]

        info = {}
        active_user = request.session.get('active_user',None)

        if Userdetail.objects.filter(username = active_user):
            user_s = Userdetail.objects.filter(username = active_user)
            info['users'] = user_s
            skills = user_s.values('skills')[0]['skills'].split(",")
            info['skills'] = skills

        if Projectdetail.objects.filter(username = active_user ):
            projects = Projectdetail.objects.filter(username = active_user )
            info['allprojects'] = projects

        if Educationdetail.objects.filter(username = active_user):
            education = Educationdetail.objects.filter(username = active_user)
            info['users_education'] = education

        if Contactdetail.objects.filter(username = active_user):
            contact = Contactdetail.objects.filter(username = active_user)
            info['contacts'] = contact

        if WorkDetail.objects.filter(username = active_user):
            work = WorkDetail.objects.filter(username = active_user)
            info['works'] = work

        if Servicedetails.objects.filter(username = active_user):
            service = Servicedetails.objects.filter(username = active_user)
            info['services'] = service
        
        return render(request,'index.html',info)
    else:
        return render(request,'index.html')

# for sending email using django backend 

from django.core.mail import send_mail, BadHeaderError
import logging,os
from decouple import config


logger = logging.getLogger(__name__)

def e_mail(request):
    if request.method == "POST":
        name = request.POST['contactName'].capitalize()
        phone = request.POST['userPhone']
        user_message = request.POST['contactMessage']
        user_email = request.POST['contactEmail']
        subject = request.POST['contactSubject']

        sender_email = os.environ.get('EMAIL_HOST_USER', '')
        receiver_mail = "mohit.dev.new@gmail.com"

        # Construct the email body
        body = f'''Hey Dude,\n{name} had sent you a message through your portfolio website.
        \n\n{user_message}\n\nSender's details:\nName: {name}\nContact Number: {phone}\nEmail: {user_email}'''

        try:
            # Use Django's send_mail function
            send_mail(subject, body, sender_email, [receiver_mail], fail_silently=False)
            email_message = "Your message was sent successfully. You will receive a response within 24 hours."
        except BadHeaderError as e:
            logger.error(f"BadHeaderError: {e}")
            email_message = "An error occurred while sending the email. Please try again later."
        request.session['email_message'] = email_message
        return redirect('show_popup')
    else:
        return redirect('/')



def show_popup(request):
    # Retrieve the email message from the session
    email_message = request.session.pop('email_message', None)

    if email_message:
        # You can pass the email message to the template context if needed
        return render(request, 'popup.html', {'email_message': email_message})
    else:
        # Handle the case where there is no email message
        return redirect('/')