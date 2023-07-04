from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.contrib import auth
from django.contrib.auth import forms

#class based view login
class Login(View)   :
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        email=request.POST.get('email')   
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
               
               #session 
               request.session['customer']=customer.id
               #session end

               if Login.return_url:
                   return HttpResponseRedirect(Login.return_url)
               else:
                   Login.return_url=None
                   return redirect('/')
               
            else:
                  error_message='Email or Password incorrect'
        else:
            error_message='Email or Password incorrect'   
        return render(request,'login.html',{'error':error_message}) 

def userlogout(request):
    auth.logout(request)
    return redirect('ulogin')

def adminlogin(request):
    return render(request,'adminlogin.html')  

def AdminLogin(request):
    if request.method=="POST":
        vuname=request.POST.get('username')             
        vpass=request.POST.get('password') 
        newuser=auth.authenticate(username=vuname,password=vpass)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/home')
        else:
            return redirect('/alogin') 
    
def adminlogout(request):
    auth.logout(request)
    return redirect('alogin')      
    
  