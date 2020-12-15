from django import forms
from .models import *

class FoodForm(forms.ModelForm):
    class Meta:
        model=RiceModel
        fields="__all__"

class CurryForm(forms.ModelForm):
    class Meta:
        model=CurryItemModel
        fields="__all__"


class Non_veg_Form(forms.ModelForm):
    class Meta:
        model=Non_veg_model
        fields="__all__"