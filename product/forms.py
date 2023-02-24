from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from product import models
from django.forms import ModelForm
from product.models import UserProfile, Product


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# class UserProfileForm(forms.ModelForm):
#     class meta:
#         model=UserProfile
#         fields=["profile_pic","phonenumber","bio"]
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'location', 'category', 'owner']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'address', 'phone', 'profile_pic']
