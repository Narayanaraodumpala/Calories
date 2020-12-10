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
    food_choices=[('Rice','Rice'),('Potato','Potato'),('Brinjal','Brinjal'),('Ladyfinger','Ladyfinger'),
                  ('beetroot','beetroot'),('capsicum','capsicum'),('mushrooms','mushrooms'),
                  ('brocoli', 'brocoli'), ('cabbage', 'cabbage'), ('carrot', 'carrot'), ('cauliflower', 'cauliflower'),
                  ('cucumber', 'cucumber'), ('garlic','garlic'),('onion','onion'),
                  ('pumpkin','pumpkin'),('string beans or green beans','string beans or green beans'),('apple','apple'),
                  ('apricot','apricot'),('avocodo','avocodo'),('banana','banana'),('blackberry','blackberry'),('cherry','cherry'),
                  ('grapes','grapes'),('green olive','green olive'),('kiwifruit','kiwifruit'),('lemon','lemon'),('lime','lime'),
                  ('mango','mango'),('orange','orange'),('papayya','papayya'),
                  ('peach','peach'),('pineapple','pineapple'),('plum','plum'),('strawberry','strawberry'),('tomatto','tomatto'),
                  ('corn','corn'),('sweet potato','sweet potato'),('watermelon','watermelon'),




                  ]

    food_type_choices=[
        ('Veg','Veg'), ('Non-Veg', 'Non-Veg'), ('Drinks', 'Drinks'),
    ]
    food = models.CharField(max_length=50, null=True,choices=food_choices)
    food_type = models.CharField(max_length=30, null=True,choices=food_type_choices)

    def __str__(self):
        return self.food

