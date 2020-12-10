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


class FoodModel(models.Model):
      food=models.CharField(max_length=50,null=True)
      food_type=models.CharField(max_length=30,null=True)
      food_image=models.ImageField(upload_to='food_images/',null=True)

      calories = models.FloatField(null=True)
      water = models.FloatField(null=True)
      protein = models.FloatField(null=True)
      carbohydrates=models.FloatField(null=True)
      sugar = models.FloatField(null=True)
      fiber = models.FloatField(null=True)
      fats=models.FloatField(null=True)
      vitamin=models.FloatField(null=True)




      def __str__(self):
          return self.food


