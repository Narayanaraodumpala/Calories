"""CaloriesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from calorieapp import urls as url, views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logouttt,name='logout'),
    path('protiens/',views.protiens,name='protiens'),
    path('vaitamins/', views.vaitamins,name='vaitamins'),
path('carbos/', views.carbos, name='carbos'),
    path('glucos/',views.glucos,name='glucos'),
    path('login_signup/',views.login_signup,name='login_signup'),
    path('bmi/',views.bmi,name='bmi'),
    path('calories/',views.calories,name='calories')
]
