from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
          return render(request,'signup.html')
    
    def post(self,request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        
        #validation
        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        error_message = None

        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password) 
        error_message=self.validateCustomer(customer)
        
        #saving
        if (not error_message):
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            datas={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',datas)
        
    def validateCustomer(self,customer):
        error_message=None

        if(not customer.first_name):
            error_message="First name required"
        elif len(customer.first_name)<4:
            error_message='First name must be 4 char long or more'
        elif (not customer.last_name):
            error_message="last name required"
        elif len(customer.last_name)<4:
            error_message='last name must be 4 char long or more'
        elif (not customer.phone):
            error_message="phone no required"
        elif len(customer.phone)==10:
            error_message='phone must be 10 no long'
        elif len(customer.email)<5:
            error_message='email must be 5 char long or more'
        elif len(customer.password)<6:
            error_message='password must be 6 char long or more'
        elif customer.isExists():
            error_message='Email allready register'

        return error_message