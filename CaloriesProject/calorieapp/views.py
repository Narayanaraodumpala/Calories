from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from .forms import *
calories=0
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


def caloriess(request):

    return render(request,'calories.html',{'model':FoodForm()})


def food(request):
    food = request.POST['rice_item']
    type = request.POST['type']
    quantity = request.POST['quantity']
    print('food=', food)
    if food == 'Rice':
        protiens = 2
        carbos = 8
        water = 0
        sugar = 0.1
        fiber = 0.4
        fat = 0.19
        vitamin = 0.14
        print(protiens)
        print(carbos)
        global calories
        calories=int(protiens)+int(carbos)+int(water)+int(sugar)+int(fiber)+int(fat)+int(vitamin)


        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print ('cal=', cal)



        return render(request, 'Brown.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':CurryForm()})


    elif food == 'Brown-Rice':
        protiens =2.6
        carbos =23
        water =0
        sugar =0.4
        fiber =1.8
        fat =0.9
        vitamin =5
        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print ('cal=', cal)



        return render(request, 'Brown.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':CurryForm()})

    elif food == 'Biryani':
        protiens =20
        carbos =31
        water =0
        sugar =3.2
        fiber =1.8
        fat =9.4
        vitamin =5
        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print ('cal=', cal)

        return render(request, 'Brown.html', {'food': food, 'protins': protiens,
                                          'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':CurryForm()})

    elif food == 'Fride-Rice':
        protiens = 4.7
        carbos = 31
        water = 0
        sugar = 0.4
        fiber = 1.1
        fat = 2.3
        vitamin = 1
        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'Brown.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos,'water':water,'sugar':sugar,
                                              'fiber':fiber,'fat':fat,'vitamin':vitamin , 'cal': cal,'curry':CurryForm()})
    else:

        protiens = 0
        carbos = 0
        water = 0
        sugar = 0
        fiber = 0
        fat = 0
        vitamin = 0
        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'Brown.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':CurryForm()})







