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
        water=0
        sugar=0.1
        fiber=0.4
        fat=0.19
        vitamin=0.14
        print(protiens)
        print(carbos)

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})
    elif food == 'Potato':

        protiens = 2
        carbos = 17
        water = 0
        sugar = 0.8
        fiber = 2.2
        fat = 0.1
        vitamin = 47

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})
    elif food == 'Brinjal':

        protiens=1
        carbos =5
        water =0
        sugar =3.5
        fiber =3
        fat =0.2
        vitamin =8

        return render(request,'foood.html',{'food':food,'protins':protiens,'carbs':carbos})

    elif food == 'Ladyfinger':


         protiens = 1.9
         carbos =7
         water =2
         sugar =1.5
         fiber =3.2
         fat =0.2
         vitamin =62

         return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'beetroot':

        protiens =1.6
        carbos =10
        water =60
        sugar =7
        fiber =7
        fat =0.2
        vitamin =1.3
        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'capsicum':

        protiens =1.6
        carbos =10
        water =30
        sugar =7
        fiber =2.8
        fat =0.2
        vitamin =13

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'mushrooms':

        protiens =3.1
        carbos =3.3
        water =15
        sugar =2
        fiber =1
        fat =0.3
        vitamin =13

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'brocoli':

        protiens =2.8
        carbos =7
        water =20
        sugar =7
        fiber =2.6
        fat =0.4
        vitamin =170

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cabbage':

        protiens =1.3
        carbos =6
        water =25
        sugar =3.2
        fiber =2.5
        fat =0.1
        vitamin =66

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'carrot':

        protiens =0.5
        carbos =6
        water =30
        sugar =3
        fiber =2
        fat =0.7
        vitamin =30

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cauliflower':

        protiens =1.9
        carbos =5
        water =10
        sugar =1.9
        fiber =2
        fat =0.3
        vitamin =90

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cucumber':

        protiens =2
        carbos =11
        water =30
        sugar =1.5
        fiber =2
        fat =0
        vitamin =74

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'garlic':
        protiens =7.9
        carbos =16.3
        water =0
        sugar =1.7
        fiber =5.5
        fat =0.6
        vitamin =20


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'onion':
        protiens =1.1
        carbos =9
        water =0
        sugar =4.2
        fiber =1.7
        fat =0.1
        vitamin =19

        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'pumpkin':
        protiens =1
        carbos =7
        water =20
        sugar =2.8
        fiber =0.5
        fat =0.1
        vitamin =190


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'string beans or green beans':

        protiens =1.8
        carbos =7
        water =10
        sugar =0
        fiber =3.4
        fat =0.1
        vitamin =34

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'apple':
        protiens =0.3
        carbos =14
        water =20
        sugar =10
        fiber =2.4
        fat =0.2
        vitamin =8

        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'apricot':
        protiens =2
        carbos =9
        water =20
        sugar =0.7
        fiber =7
        fat =15
        vitamin =19


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'avocodo':
        protiens =2
        carbos =9
        water =20
        sugar =0.7
        fiber =7
        fat =15
        vitamin =19


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'banana':
         protiens =1.1
         carbos =23
         water =60
         sugar =12
         fiber =2.6
         fat =0.3
         vitamin =15


         print(protiens)
         print(carbos)

         return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'blackberry':
         protiens =1.4
         carbos =10
         water =10
         sugar =4.9
         fiber =5
         fat =0.5
         vitamin =41

         return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'cherry':
        protiens =2
        carbos =25
        water =60
        sugar =0
        fiber =3
        fat =0
        vitamin =18


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'grapes':
        protiens =1.1
        carbos =27.3
        water =65
        sugar =0
        fiber =1.4
        fat =0.2
        vitamin =53


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'green olive':
        protiens =1.1
        carbos =27.3
        water =65
        sugar =0
        fiber =1.4
        fat =0.2
        vitamin =53


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'kiwifruit':
        protiens =1.1
        carbos =15
        water =70
        sugar =9
        fiber =3
        fat =0.3
        vitamin =161


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'lemon':
        protiens =1.1
        carbos =9
        water =90
        sugar =2.5
        fiber =2.8
        fat =0.3
        vitamin =5


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'lime':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'mango':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'orange':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'papayya':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'peach':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'pineapple':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'plum':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'strawberry':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'tomatto':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =


        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'corn':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =

        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'sweet potato':
        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =

        print(protiens)
        print(carbos)

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
    elif food == 'watermelon':

        protiens =
        carbos =
        water =
        sugar =
        fiber =
        fat =
        vitamin =

        return render(request, 'foood.html', {'food': food, 'protins': protiens, 'carbs': carbos})
