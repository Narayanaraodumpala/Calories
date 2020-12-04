from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userdetails(models.Model):
    auth_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)
    address=models.CharField(max_length=50,null=True)


class BMIModel(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bmi=models.CharField(max_length=20,null=True)
    date=models.DateTimeField(auto_now_add=True)