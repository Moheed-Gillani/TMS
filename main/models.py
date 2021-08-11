from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    shop_address=models.CharField(max_length=50,null=True)
    Name=models.CharField(max_length=10,blank=True)
    Image=models.ImageField(null=True)
    def __str__(self):
        return str(self.Name)
class profiles_order(models.Model):
    to_tailor=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    customer_name=models.CharField(max_length=50,null=True)
    customer_email=models.EmailField(null=True)
    customer_contact=models.IntegerField(null=True)
    shipping_address=models.CharField(max_length=100,null=True)
    Qameez_length_inch=models.IntegerField(null=True)
    Chest_Size_inch=models.IntegerField(null=True)
    Sleves_lengt_inch=models.IntegerField(null=True)
    def __str__(self):
        return self.customer_name
# Create Profiles Posts here.
class Post(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image=models.ImageField(null=True)
    headline=models.CharField(max_length=200)
    price=models.IntegerField(null=True,default=100)
    text=models.TextField()
    date=models.DateField(auto_created=True,null=True)
    def __str__(self):
        return self.headline
    
class post_orders(models.Model):
    design=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    customer_name=models.CharField(max_length=50,null=True)
    customer_email=models.EmailField(null=True)
    customer_contact=models.IntegerField(null=True)
    shipping_address=models.CharField(max_length=100,null=True)
    Qameez_length_inch=models.IntegerField(null=True)
    Chest_Size_inch=models.IntegerField(null=True)
    Sleves_lengt_inch=models.IntegerField(null=True)
    def __str__(self):
        return self.customer_name

# Create Profiles models here.
class Comment(models.Model):
    on_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()
    name=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    on=models.DateField(null=True,auto_now=True)
    def __str__(self):
        return self.comment
class Reply(models.Model):
    on_comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    Reply=models.TextField()
    name=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    on=models.DateField(null=True,auto_now=True)
    def __str__(self):
        return self.Reply





