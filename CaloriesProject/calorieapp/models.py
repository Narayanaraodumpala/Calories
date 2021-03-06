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


curry_choices=[('Nothing', 'Nothing') ,('Potato','Potato'),('Brinjal','Brinjal'),('Ladyfinger','Ladyfinger'),
                  ('beetroot','beetroot'),('capsicum','capsicum'),('mushrooms','mushrooms'),
                  ('brocoli', 'brocoli'), ('cabbage', 'cabbage'), ('carrot', 'carrot'), ('cauliflower', 'cauliflower'),
                  ('cucumber', 'cucumber'), ('garlic','garlic'),('onion','onion'),
                  ('pumpkin','pumpkin'),('string beans or green beans','string beans or green beans'),




                  ]

food_type_choices=[
    ('Nothing', 'Nothing'), ('Veg','Veg'), ('Non-Veg', 'Non-Veg'), ('Drinks', 'Drinks'),
    ]
salad_choices=[
    ('Nothing', 'Nothing'), ('apple', 'apple'),
        ('apricot', 'apricot'), ('avocodo', 'avocodo'), ('banana', 'banana'), ('blackberry', 'blackberry'),
        ('cherry', 'cherry'),
        ('grapes', 'grapes'), ('green olive', 'green olive'), ('kiwifruit', 'kiwifruit'), ('lemon', 'lemon'),
        ('lime', 'lime'),
        ('mango', 'mango'), ('orange', 'orange'), ('papayya', 'papayya'),
        ('peach', 'peach'), ('pineapple', 'pineapple'), ('plum', 'plum'), ('strawberry', 'strawberry'),
        ('tomatto', 'tomatto'),
        ('corn', 'corn'), ('sweet potato', 'sweet potato'), ('watermelon', 'watermelon'),
    ]
non_veg_choices=[
    ('Nothing', 'Nothing'), ('Chicken', 'Chicken'), ('Egg', 'Egg'), ('Mutton', 'Mutton'),('Fish', 'Fish'), ('Crabs', 'Crabs'),('Prawns', 'Prawns')
    ]
drink_choices=[
    ('Nothing', 'Nothing'), ('Water', 'Water'), ('Milk', 'Milk'), ('Butter-Milk', 'Butter-Milk'), ('Coakes', 'Coakes'),
    ]
rice_item_choices=[
    ('Nothing', 'Nothing') , ('Rice', 'Rice'), ('Fride-Rice', 'Fride-Rice'), ('Brown-Rice', 'Brown-Rice'), ('Biryani', 'Biryani'),
    ]

class FoodModel(models.Model):

    food_type = models.CharField(max_length=30, null=True, choices=food_type_choices)
    rice_item=models.CharField(max_length=30,choices=rice_item_choices,null=True)

    curry = models.CharField(max_length=50, null=True,choices=curry_choices)

    salad=models.CharField(max_length=30,choices=salad_choices,null=True)
    non_veg=models.CharField(max_length=30,choices=non_veg_choices,null=True)
    drinks=models.CharField(max_length=50,choices=drink_choices,null=True)


    def __str__(self):
        return self.curry



class RiceModel(models.Model):

    rice_item=models.CharField(max_length=30,choices=rice_item_choices,null=True)
    type=models.CharField(max_length=30,choices=food_type_choices,null=True)
    quantity=models.CharField(max_length=30,null=True)



class CaloriesModel(models.Model):
    food_cal=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.food_cal


class CurryItemModel(models.Model):

    curry_item=models.CharField(max_length=30,choices=curry_choices,null=True)
    curry_type=models.CharField(max_length=30,choices=food_type_choices,null=True)
    quantity=models.CharField(max_length=30,null=True)


class Non_veg_model(models.Model):

    non_veg_item=models.CharField(max_length=30,choices=non_veg_choices,null=True)
    type=models.CharField(max_length=30,choices=food_type_choices,null=True)
    quantity=models.CharField(max_length=30,null=True)





