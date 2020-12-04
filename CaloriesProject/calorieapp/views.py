from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
# Create your views here.
def signup(request):
    error=False
    if request.method=='POST':

        usr=request.POST['user']
        pwd=request.POST['pwd']
        mob=request.POST['mob']
        img=request.FILES['img']
        add=request.POST['add']
        email=request.POST['email']
        userdata=User.objects.filter(username=usr)
        if not userdata:
           user= User.objects.create_user(username=usr,password=pwd,email=email)
           Userdetails.objects.create(auth_user=user,image=img,address=add,mobile=mob)
        else:
            error=True
    return render(request,'signup.html',{'error':error})


def protiens(request):
    return render(request,'protiens.html')


def vaitamins(request):
    return render(request,'vaitamins.html')


def carbos(request):
    return render(request, 'carbos.html')


def glucos(request):
    return render(request, 'glucos.html')


def login_signup(request):
    error=False
    if request.method == 'POST':
        dic=request.POST
        usr=dic['user']
        pwdr=dic['pwd']
        user=authenticate(username=usr,password=pwdr)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error=True
    return render(request,'login_sigup.html',{'error':error})


def logouttt(request):
    logout(request)
    return redirect('home')


def bmi(request):
    hgt=request.POST['height']
    wgt=request.POST['weight']

    mts=int(hgt) / 100
    meter_sq=(mts)*(mts)
    bmi=int(wgt) / meter_sq
    print('bmi=',bmi)
    user=request.user
    BMIModel.objects.create(usr=user,bmi=bmi)

    return render(request, 'bmi.html',{'bmi':bmi})


def calories(request):
    return render(request,'calories.html')