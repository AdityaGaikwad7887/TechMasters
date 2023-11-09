from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def home(request):
    global dict
    dict = {'user':request.user,
            'dir':''}     
    return render(request,'index.html')

def about(request):
    return render(request,'about.html',dict)

def contact(request):
    return render(request,'contact.html',dict)

def products(request):
    return render(request,'products.html',dict)

def services(request):
    return render(request,'services.html',dict)

def log_out(request):
    logout(request)
    dict.update({'user': request.user})
    # messages.success(request,'logout succesfully')
    return render(request , 'index.html',dict)

def sign_in(request):
    dict.update({'dir':'SignIn'})
         
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mob_no')
        location = request.POST.get('location')
        user_type = request.POST.get('user_type')
        
        
        user = User.objects.create_user(username = username, email = email , password = password)
        user.save()
        login(request ,user)
        print(user.is_authenticated)
        dict.update({'user': request.user})
        
        if(user_type == "Labour"):
            skills = request.POST.get('skills')
            
            profession = request.POST.get('profession')
            user1 = LabourUser(username = username,email = email,password=password,mobile = mobile,location=location , skills = skills,profession=profession)
            user1.save()

        else :
            user1 = NormalUser(username = username,email = email,password=password,mobile = mobile,location=location)
            user1.save()    
        
             
        return render(request,'index.html',dict)

    return render(request,"index.html",dict)

def log_in(request):
    dict.update({'dir':"login",
           'user':request.user})
   
    if request.method == "POST":
        username = request.POST.get('username')
        
        password = request.POST.get('password')

        user =authenticate(username =username , password = password)

        if user is not None:
            login(request ,user)
            print(user.is_authenticated)
            messages.success(request , "successfully logged in")
            dict.update({'user':request.user})
            # img =Image.objects.all()
            return render(request, 'index.html',dict)
        else :
            messages.success(request , "invalid credential")    

    return render(request,"index.html",dict)