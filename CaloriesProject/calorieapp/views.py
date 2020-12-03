from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'signup.html')


def protiens(request):
    return render(request,'protiens.html')


def vaitamins(request):
    return render(request,'vaitamins.html')


def carbos(request):
    return render(request, 'carbos.html')


def glucos(request):
    return render(request, 'glucos.html')