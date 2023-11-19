from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    global dict
    dict = {'user':request.user,
            'dir':'',
            'userType':''}   
    
    allProdImages = ProductImage.objects.all()
    dict['ProductIMAGE'] = allProdImages    
    
    return render(request,'index.html',dict)

def home(request):
    allProdImages = ProductImage.objects.all()
    dict['ProductIMAGE'] = allProdImages    
    return render(request,'index.html',dict)

def about(request):
    allLabourUser = LabourUser.objects.all()
    
    dict['data'] = allLabourUser
    return render(request,'about.html',dict)

def contact(request):
    return render(request,'contact.html',dict)


def services(request):
    allServImages = ServiceImage.objects.all()
    dict['ServImage'] = allServImages
    # if request.method == "GET":
        
    
    return render(request,'services.html',dict)

def log_out(request):
    logout(request)
    dict.update({'user': request.user})
    messages.success(request,'logout succesfully')
    return HttpResponseRedirect('/home')

def sign_in(request):
    dict.update({'dir':'SignIn'})
         
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mob_no')
        location = request.POST.get('location')
        user_type = request.POST.get('user_type')
        
        user5 = User.objects.filter(username = username)
        if user5.count() != 0:
            messages.success(request,'Username Already exist try another one')
            return HttpResponseRedirect('/home')
        user = User.objects.create_user(username = username, email = email , password = password)
        user.save()
        login(request ,user)
        print(user.is_authenticated)
        dict.update({'user': request.user})
        
        
        if(user_type == "Labour"):
            skills = request.POST.get('skills')
            
            profession = request.POST.get('profession')
            user1 = LabourUser(username = username,email = email,password=password,mobile = mobile,location=location , skills = skills,profession=profession,user = user)
            dict['Luser'] = user1
            
            dict.update({'userType':'labour'})
            user1.save()
            

        else :
            user1 = NormalUser(username = username,email = email,password=password,mobile = mobile,location=location , user = user)
            user1.save()    
            dict['Luser'] = user1
            
            dict.update({'userType':'normal'})
        
        
        return HttpResponseRedirect('/home')
    
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
            user2 = NormalUser.objects.filter(username = user.username)
            print(user2)
            if user2.count() == 0:
                user1 = LabourUser.objects.get(username = user.username)
                dict.update({'userType':'labour'})
            else:
                user1 = NormalUser.objects.get(username = user.username)
                dict.update({'userType':'normal'})

            dict.update({'Luser' : user1})
            print(user.is_authenticated)
            messages.success(request , "successfully logged in")
            dict.update({'user':request.user})
            # img =Image.objects.all()
            return HttpResponseRedirect('/home') 
        else :
            messages.success(request , "invalid credential")  

            

    return render(request,"index.html",dict)


def LabourList(request,serviceType):
    print(serviceType)
    labours = LabourUser.objects.filter(profession = serviceType)
    return render(request,'laborList.html',{'labours':labours , 'serviceType' : serviceType})

def quizFun(request):
    if request.method == "POST":
        score = request.POST.get('score')
        print(score)
        print("hi")
        user1 = LabourUser.objects.get(username = request.user.username)
        user1.score =user1.score+ int(score)
        user1.save()
        dict.update({'Quize':False})
       
        dict.update({'Luser' : user1})
        return HttpResponseRedirect('/home')
    user1 = LabourUser.objects.get(username = request.user.username)
    quiz1 = quiz.objects.get(service = user1.profession)
    questions2 = []
    questions1 = questions.objects.filter(quiz = quiz1)
    
    
    for question1 in questions1:
        ans2 = []
        ans = Answer.objects.filter(questions = question1)
        for answ in ans:
            ans2.append(answ.text)
        ans1 = Answer.objects.get(questions = question1,correct = True)
        questions2.append({question1.text : {ans1 : ans2}})
        
       
    dict['Qdata'] = questions2
    dict['Quize'] = True    

    return render(request ,'Quiz.html' , dict);   
      

        
    