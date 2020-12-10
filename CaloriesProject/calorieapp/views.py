from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from .forms import *
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
           user=User.objects.create_user(username=usr,password=pwd,email=email)
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

    return render(request,'calories.html',{'model':FoodForm()})

def food(request):
    food=request.POST['food']
    food_type = request.POST['food_type']
    print('food=',food)
    if food == 'Rice':
        protiens=2
        carbos=8
        print(protiens)
        print(carbos)

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})
    elif food == 'Potato':

        protiens=10
        carbos=8
        print(protiens)
        print(carbos)

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})
    elif food == 'Brinjal':

        protiens=0
        carbos=80
        print(protiens)
        print(carbos)

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})
    elif food == 'Ladyfinger':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'beetroot':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'capsicum':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'mushrooms':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'brocoli':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cabbage':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'carrot':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cauliflower':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cucumber':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'garlic':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'onion':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'pumpkin':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'string beans or green beans':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'apple':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'apricot':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'avocodo':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'banana':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'blackberry':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cherry':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'grapes':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'green olive':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'kiwifruit':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'lemon':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'lime':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'mango':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'orange':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'papayya':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'peach':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'pineapple':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'plum':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'strawberry':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'tomatto':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'corn':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'sweet potato':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'watermelon':

        protiens = 0
        carbos = 80
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
        