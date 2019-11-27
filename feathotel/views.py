from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Enquery

# Create your views here.
def show(request):
    return render(request,"index.html")
def enquery(request):
    if request.method=="POST":
        if request.POST.get('fname') and request.POST.get('email') and request.POST.get('contactNum') and request.POST.get('query'):
            post=Enquery()
            post.fname= request.POST.get('fname')
            post.lname= request.POST.get('lname')
            post.email= request.POST.get('email')
            post.contactNum= request.POST.get('contactNum')
            post.query= request.POST.get('query')
            post.save()
            return redirect('')
        else:
            return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already exists')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request,'this email is used')
                return redirect('signup')
            
            else:
                user=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
                user.save()
                
                return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('signup')
            
        
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user not valid')
            return redirect('/login')

    else:    
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return render(request,"index.html")

