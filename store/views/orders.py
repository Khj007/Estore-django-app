from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

#class based view login
class Orders(View):
    def get(self,request):
       customer=request.session.get('customer')
       orders=Order.get_orders_by_customer(customer)
       return render(request,'orders.html',{'orders':orders})
