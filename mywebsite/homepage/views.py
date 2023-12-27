from django.shortcuts import render,redirect
from django.http import HttpResponse
from userdata.models import Educationdetail,Userdetail,Contactdetail,Projectdetail
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
        
        return render(request,'index.html',info)
    else:
        return render(request,'index.html')

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def e_mail(request):
    if request.method=="POST":
            name = request.POST['contactName'].capitalize()
            phone = request.POST['userPhone']
            user_message = request.POST['contactMessage']
            user_email = request.POST['contactEmail']
            subject = request.POST['contactSubject']

            sender_email = "ananonymousking1@gmail.com"
            sender_password = "xsikqqfbahtvvtqf"
            receiver_mail = "mohit.dev.new@gmail.com"

            # Create a message object
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_mail
            message["Subject"] = subject

            # Add body text to the email
            body = f'''Hey Dude,\n{name} had send you a message through your portfolio website.
            \n\n{user_message}\n\nSender's details : \nName: {name}\nContact Number:{phone}\nemail: {user_email}'''
            message.attach(MIMEText(body, "plain"))
            try:
                # Create the SMTP server and login
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)

                # Send the email and close the connection
                text = message.as_string()
                server.sendmail(sender_email, receiver_mail, text)
                messages.success(request, "Your message was sent successfully. You'll receive a response within 24 hours.")

            except Exception as e:
                print(e)

            finally:
                server.quit()
            return redirect('/')