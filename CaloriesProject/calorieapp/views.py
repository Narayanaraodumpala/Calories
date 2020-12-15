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


def curry(request):
    food = request.POST['curry_item']
    type = request.POST['curry_type']
    quantity = request.POST['quantity']

    if food == 'Potato':

        protiens = 2
        carbos = 17
        water = 0
        sugar = 0.8
        fiber = 2.2
        fat = 0.1
        vitamin = 47

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry': Non_veg_Form()
                                              })
    elif food == 'Brinjal':

        protiens = 1
        carbos = 5
        water = 0
        sugar = 3.5
        fiber = 3
        fat = 0.2
        vitamin = 8

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'foood.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})

    elif food == 'Ladyfinger':

        protiens = 1.9
        carbos = 7
        water = 2
        sugar = 1.5
        fiber = 3.2
        fat = 0.2
        vitamin = 62

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'beetroot':

        protiens = 1.6
        carbos = 10
        water = 60
        sugar = 7
        fiber = 7
        fat = 0.2
        vitamin = 1.3
        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'capsicum':

        protiens = 1.6
        carbos = 10
        water = 30
        sugar = 7
        fiber = 2.8
        fat = 0.2
        vitamin = 13

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'mushrooms':

        protiens = 3.1
        carbos = 3.3
        water = 15
        sugar = 2
        fiber = 1
        fat = 0.3
        vitamin = 13
        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})


    elif food == 'brocoli':

        protiens = 2.8
        carbos = 7
        water = 20
        sugar = 7
        fiber = 2.6
        fat = 0.4
        vitamin = 170

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'cabbage':

        protiens = 1.3
        carbos = 6
        water = 25
        sugar = 3.2
        fiber = 2.5
        fat = 0.1
        vitamin = 66

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'foood.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'carrot':

        protiens = 0.5
        carbos = 6
        water = 30
        sugar = 3
        fiber = 2
        fat = 0.7
        vitamin = 30

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'cauliflower':

        protiens = 1.9
        carbos = 5
        water = 10
        sugar = 1.9
        fiber = 2
        fat = 0.3
        vitamin = 90

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'cucumber':

        protiens = 2
        carbos = 11
        water = 30
        sugar = 1.5
        fiber = 2
        fat = 0
        vitamin = 74
        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})


    elif food == 'garlic':
        protiens = 7.9
        carbos = 16.3
        water = 0
        sugar = 1.7
        fiber = 5.5
        fat = 0.6
        vitamin = 20

        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'onion':
        protiens = 1.1
        carbos = 9
        water = 0
        sugar = 4.2
        fiber = 1.7
        fat = 0.1
        vitamin = 19

        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'pumpkin':
        protiens = 1
        carbos = 7
        water = 20
        sugar = 2.8
        fiber = 0.5
        fat = 0.1
        vitamin = 190

        print(protiens)
        print(carbos)

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request,'foood.html' , {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                              'curry': Non_veg_Form()})
    elif food == 'string beans or green beans':

        protiens = 1.8
        carbos = 7
        water = 10
        sugar = 0
        fiber = 3.4
        fat = 0.1
        vitamin = 34

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'foood.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})
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
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':Non_veg_Form()})


def non_veg(request):
    food = request.POST['non_veg_item']
    type = request.POST['type']
    quantity = request.POST['quantity']

    if food == 'Chicken':
        protiens = 47
        carbos = 8
        water = 0
        sugar = 0.1
        fiber = 0.4
        fat =14
        vitamin = 0.14
        print(protiens)
        print(carbos)
        global calories
        calories=int(protiens)+int(carbos)+int(water)+int(sugar)+int(fiber)+int(fat)+int(vitamin)


        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print ('cal=', cal)



        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                              'carbs': carbos, 'water': water, 'sugar': sugar,
                                              'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,'curry':CurryForm()})
    elif food == 'Egg':

        protiens = 6
        carbos = 0.7
        water = 0
        sugar = 0.6
        fiber = 0
        fat = 5
        vitamin = 35

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})
    elif food == 'Mutton':

        protiens = 59
        carbos = 7
        water = 0
        sugar = 0
        fiber = 3.4
        fat = 51
        vitamin = 180

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})
    elif food == 'Fish':

        protiens = 39
        carbos = 7
        water = 10
        sugar = 0
        fiber = 3.4
        fat = 22
        vitamin = 160

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})
    elif food == 'Crabs':

        protiens = 17.88
        carbos = 0
        water = 79.8
        sugar = 0
        fiber = 3.4
        fat = 41
        vitamin = 120

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})
    elif food == 'Prawns':

        protiens = 27.88
        carbos = 0
        water = 39.8
        sugar = 0
        fiber = 30.4
        fat = 21
        vitamin = 150

        calories = int(protiens) + int(carbos) + int(water) + int(sugar) + int(fiber) + int(fat) + int(vitamin)

        CaloriesModel.objects.create(food_cal=calories)
        cal = CaloriesModel.objects.get(food_cal=calories)
        print('cal=', cal)

        return render(request, 'non_veg.html', {'food': food, 'protins': protiens,
                                           'carbs': carbos, 'water': water, 'sugar': sugar,
                                          'fiber': fiber, 'fat': fat, 'vitamin': vitamin, 'cal': cal,
                                          'curry': Non_veg_Form()})



