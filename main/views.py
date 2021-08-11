from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from main.forms import profilecreater,CreateBlogs,design_order
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from main.models import *
from django.utils import timezone
from django.views.generic.edit import UpdateView,FormView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect,HttpResponse

def profileorder(request,pk):
    form=design_order()
    if request.method=='POST':
        form=design_order(request.POST or request.GET)
        if form.is_valid():
            customer_name=request.POST['customer_name']
            customer_email=request.POST['customer_email']
            customer_contact=request.POST['customer_contact']
            shipping_address=request.POST['shipping_address']
            Qameez_length_inch=request.POST['Qameez_length_inch']
            Chest_Size_inch=request.POST['Chest_Size_inch']
            Sleves_lengt_inch=request.POST['Sleves_lengt_inch']
            taillor=Profiles.objects.get(pk=pk)
            profiles_order.objects.create(to_tailor=taillor,customer_name=customer_name,customer_email=customer_email,customer_contact=customer_contact,shipping_address=shipping_address,Qameez_length_inch=Qameez_length_inch,Chest_Size_inch=Chest_Size_inch,Sleves_lengt_inch=Sleves_lengt_inch)
            return render(request,'posts/profile_order_success.html',{'tailor':taillor})
    else:
        return render(request,'posts/design_order.html',{'form':form})
            
            

def designorder(request,pk):
    form=design_order()
    if request.method=='POST':
        form=design_order(request.POST or request.GET)
        if form.is_valid():
            customer_name=request.POST['customer_name']
            customer_email=request.POST['customer_email']
            customer_contact=request.POST['customer_contact']
            shipping_address=request.POST['shipping_address']
            Qameez_length_inch=request.POST['Qameez_length_inch']
            Chest_Size_inch=request.POST['Chest_Size_inch']
            Sleves_lengt_inch=request.POST['Sleves_lengt_inch']
            design=Post.objects.get(pk=pk)
            post_orders.objects.create(design=design,customer_name=customer_name,customer_email=customer_email,customer_contact=customer_contact,shipping_address=shipping_address,Qameez_length_inch=Qameez_length_inch,Chest_Size_inch=Chest_Size_inch,Sleves_lengt_inch=Sleves_lengt_inch)
            return render(request,'posts/design_order_success.html',{'post':design})
        
    else:
        return render(request,'posts/design_order.html',{'form':form})
    
    
@require_http_methods("POST")
def reply(request,pk):
    if request.method=='POST':
        user=request.POST['username']
        reply=request.POST['Reply']
        comment=Comment.objects.get(pk=pk)
        profile=Profiles.objects.get(Name=user)
        Reply.objects.create(on_comment=comment, Reply=reply,name=profile,on=timezone.now())
        return HttpResponseRedirect('/')
    return render(request,'posts/posts.html',)

@require_http_methods("POST")
def comment(request,pk):
    if request.method=='POST':
        user=request.POST['username']
        comment=request.POST['comment']
        profile=Profiles.objects.get(Name=user)
        post=Post.objects.get(pk=pk)
        Comment.objects.create(on_post=post, comment=comment, name=profile, on=timezone.now())
        return HttpResponseRedirect('/')
    return render(request,'posts/posts.html',)
        
def  Myblogs(request,pk):
    if request.method == 'GET':
        user=User.objects.get(pk=pk)
        Blogs=Post.objects.filter(posted_by=user)
        return render(request,'posts/myblogs.html',{'blogs':Blogs})
def CreateBlog(request,pk):
    if request.method=='POST':
        form=CreateBlogs(request.POST,request.FILES)
        if form.is_valid():
            user=User.objects.get(pk=pk)
            Photo=request.FILES['Photo']
            Headline=request.POST['Headline']
            price=int(request.POST['price'])
            text=request.POST['Post']
            Post.objects.create(posted_by=user,image=Photo,headline=Headline,price=price,text=text,date=timezone.now())
            return redirect('/')
        else:
            form=CreateBlog()
            return render(request,'posts/createblog.html',{'form':form})
    form=CreateBlogs()
    return render(request,'posts/createblog.html',{'form':form})
class HomePageView(TemplateView):
    template_name='posts/posts.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Blogs']=Post.objects.all()
        return context
    
class ProfileView(TemplateView):
    template_name='posts/profiles.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['profiles']=Profiles.objects.all()
        return context
class RegisterView(View):
    def get(self, request):
        form=profilecreater()
        return render(request,'registration/register.html',{'form':form})
    def post(self, request):
        form=profilecreater(request.POST,request.FILES)
        if form.is_valid():
            Name=request.POST['Name']
            Email=request.POST['Email']
            Password=request.POST['Password']
            ConfirmPassword=request.POST['ConfirmPassword']
            Profile_Pic=request.FILES['Profile_Pic']
            Shop_address=request.POST['shop_address']
            if Password==ConfirmPassword:
                user=User.objects.create_user(Name,Email,ConfirmPassword)
                user.save()
                users=authenticate(request,username=Name,password=ConfirmPassword)
                Profiles.objects.create(User=user,shop_address=Shop_address,Name=Name,Image=Profile_Pic)
                if users is not None:
                    login(request,users)
                    return redirect('/')
            else:
                return render(request,'registration/register.html',{'error': '!Incorrect Password is not matching'})
  
            

        else:
            form=profilecreater()
            return render(request,'registration/register.html',{'error': 'Invalid forms field'})
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    login_url='accounts/login'
    redirect_field_name='home'
    model=Profiles
    fields=['Name','shop_address','Image',]
    template_name='profiles/updateprofile.html'
    success_url='/'
class BlogUpdateView(UpdateView):
    model=Post
    fields=['image','headline','price','text']
    template_name='posts/updateblog.html'
    success_url='/'

class DeleteBlogView(DeleteView):
    model=Post
    template_name='posts/post_confirm_delete.html'
    success_url='/'
  

    
        
        
 
        
       