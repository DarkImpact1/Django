from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from .models import Userdetail,Educationdetail,Projectdetail,Contactdetail,WorkDetail,Servicedetails



# Create your views here.

def register(request):
    if (request.method == 'POST'):
        f_name = request.POST["firstName"].capitalize()
        l_name = request.POST["lastName"].capitalize()
        u_name = request.POST["username"]
        e_mail = request.POST["email"].lower()
        pass1 = request.POST["password"]
        cpass = request.POST["confirmPassword"]
        # print(f_name,l_name,u_name,e_mail,pass1,cpass)
        if (pass1 == cpass):
            if( User.objects.filter(email = e_mail).exists()):
                messages.info(request,"Email Alread registered")
                return redirect("register")
                # return HttpResponse("Email Already registered")
            elif (User.objects.filter(username = u_name)).exists():
                messages.info(request,"Username taken choose another")
                return redirect("register")
                # return HttpResponse("Username already taken")
            else:
                user = User.objects.create_user(username=u_name,email=e_mail,password=cpass,first_name = f_name, last_name = l_name )
                user.save()
                # as soon as the user is created I'm redirecting it to the login page/
                return redirect('login')
         
        else:
            messages.info(request, "Password not matching")
            return redirect("register")
            # return HttpResponse("Password were not same !")
            # return render(request,'register.html')  
    else:
        print(request.method)
        return render(request, 'register.html')
    

def login(request):
    if (request.method == 'POST'):
        l_username = request.POST['loginusername']
        l_password = request.POST['loginpassword']
        if (User.objects.filter(username = l_username)).exists():
            user = auth.authenticate(username=l_username,password=l_password)
            # it will return none if credentials do not match
            if user is not None:
                auth.login(request,user)
                request.session['active_user'] = l_username

                return redirect('/')
            else:
                messages.info(request,"Invalid credentials")
                return redirect('login') 
        else:
            messages.error(request,"Kindly Register First!")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
   
def user_details(request):
    if (request.method == 'POST'):
        user_detail = Userdetail(username = request.session['active_user'],
                                full_name = request.POST["name"].capitalize(),
                                e_mail = request.POST["email"].lower(),
                                skills = request.POST["skills"],
                                profile_photo = request.FILES["profilephoto"],
                                bio = request.POST["bio"],
                                carrer_goal = request.POST['career_goal']
                                )

        try:
            user_detail.save()           
            return redirect('contactdetails')
        except Exception as e:
            print(e)
        # return HttpResponse("Your are here at user details ")
    else:
        return render(request,'details.html')
    

def contact_details(request):
    if (request.method == 'POST'):
        contactdetails = Contactdetail(
        username = request.session['active_user'],
        linkedin = request.POST['linkedin'],
        twitter = request.POST['twitter'],
        github = request.POST['github'],
        facebook = request.POST['facebook'],
        instagram = request.POST['instagram'],
        whatsapp = request.POST['whatsapp'],
        phone = request.POST['contact'],
        address = request.POST['address'],
            )
        contactdetails.save()
        return redirect('educationdetails')
    else:
        return render(request,'contacts.html')

def education_details(request):
    if (request.method == 'POST'):
        educationdetails = Educationdetail(username =request.session['active_user'],
                                           college_name = request.POST['collegeName'].title(),
                                           degree_name = request.POST['degreeName'],
                                           college_start_year = request.POST['collegeStart'],
                                           college_end_year = request.POST['collegeEnd'],
                                           about_college = request.POST['aboutCollege'],
                                           
                                           xii_school_name = request.POST['12thSchoolName'].title(),
                                           xii_school_board_name = request.POST['12thBoard'],
                                           xii_school_start = request.POST['12thStart'],
                                           xii_school_end = request.POST['12thEnd'],
                                           about_xii_school = request.POST['about12th'],
                                           
                                           x_school_name = request.POST['10thSchoolName'].title(),
                                           x_school_board_name = request.POST['10thBoard'],
                                           x_school_start = request.POST['10thStart'],
                                           x_school_end = request.POST['10thEnd'],
                                           about_x_school = request.POST['about10th'],
                                           )
        try:
            educationdetails.save()
            return redirect('projectdetails')
        except Exception as e:
            print(e)
            return HttpResponse("got some error")
    else:
        # print("rendering edacation.html")
        return render(request,'education.html')
    
def project_details(request):
    if (request.method == 'POST'):
        projectdetails = Projectdetail(
        username = request.session['active_user'],
        name = request.POST['projectname'].title(),
        description = request.POST['description'],
        image = request.FILES['image'],
        htmlid = request.POST['htmlid'],
        href = request.POST['href'],
        category = request.POST['category'].upper(),
        link = request.POST['link'])

        projectdetails.save()
        messages.info(request,"Project details Saved ")
        return redirect('projectdetails')
    else:
        return render(request,'projects.html')
    
def work_details(request):
    if (request.method == 'POST'):
        workdetais = WorkDetail(
        username = request.session['active_user'],
        jobname = request.POST['jobname'].title(),
        location = request.POST['location'].title(),
        l_skills = request.POST['skills'].upper(),
        description = request.POST['description'])
        # workdetais.save()
        messages.info(request,"Work details Saved ")
        return redirect('workdetails')  
    else:
        return render(request,'work.html')
    
def service_details(request):
    if (request.method == 'POST'):
        servicedetails = Servicedetails(
        username = request.session['active_user'],
        servicename = request.POST['service'].title(),
        description = request.POST['description'])
        # servicedetails.save()
        messages.info(request,"Service details Saved ")
        return redirect('servicedetails')
    return render(request,'services.html')