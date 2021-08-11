from django import forms
from django.contrib.auth.forms import UserCreationForm


class profilecreater(forms.Form):
    Name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
    Profile_Pic=forms.ImageField()
    shop_address=forms.CharField(max_length=100)

class CreateBlogs(forms.Form):
    Photo=forms.ImageField()
    Headline=forms.CharField(max_length=200)
    price=forms.IntegerField()
    Post=forms.CharField(widget=forms.Textarea)
class design_order(forms.Form):
    customer_name=forms.CharField()
    customer_email=forms.EmailField()
    customer_contact=forms.IntegerField()
    shipping_address=forms.CharField()
    Qameez_length_inch=forms.IntegerField()
    Chest_Size_inch=forms.IntegerField()
    Sleves_lengt_inch=forms.IntegerField()
    

    
