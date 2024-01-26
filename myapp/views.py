from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate

# Create your views here.
def homepage(request):
    return redirect('show')

def Registerpage(request):
    return render(request,'app/register.html')

def LoginPage(request):
    return render(request,'app/login.html')

def registerUser(request):
    if request.method == 'POST':
        # fname = request.POST['fname']
        # lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        print(username)

        user = User.objects.filter(username=username)
        if user:
            message = "User already exists"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create_user(username=username,email=email,password=password)
                message = "User registered successfully, Please sign in"
                return render(request,"app/login.html",{'msg':message})

def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user_profile = User.objects.get(username=username)

        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            # request.session['fname'] = user.firstname
            # request.session['lname'] = user.lastname
            login(request,user)
            # us = Description.objects.get(user=request.user)
            # request.session['content'] = us.content
            return redirect('show')
        else:
            message = 'Enter correct password'
            return render(request,'app/login.html',{'msg':message})


def insertData(request):
    # print(request.user.id)
    # print(request.user)
    content = request.POST.get('content')
    cont = Description(user=request.user, content=content)
    cont.save()
    return redirect ('show')

def showPage(request):
    all_data = Description.objects.filter(user=request.user)
    return render(request, "app/index.html", {'key1' : all_data})

def deleteData(request,pk):
    ddata=Description.objects.get(id=pk)
    ddata.delete()
    return redirect('show')

def logoutUser(request):
    logout(request)
    return render(request,'app/login.html')

def UpdateData(request,pk):
    udata = Description.objects.get(id=pk)
    udata.status = True
    udata.save()
    return redirect('show')