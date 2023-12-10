from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse


# Create your views here.
def login(request):
    if (request.method == 'POST'):
        l_username = request.POST['loginusername']
        l_password = request.POST['loginpassword']
        user = auth.authenticate(username=l_username,password=l_password)
        # it will return none if credentials do not match
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
        
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



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
    

