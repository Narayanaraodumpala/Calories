from django import forms
from .models import *

class FoodForm(forms.ModelForm):
    class Meta:
        model=FoodModel
        fields="__all__"