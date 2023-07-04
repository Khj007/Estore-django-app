from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
#class based view login
class Cart(View)   :
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_By_Id(ids)
        return render(request,'cart.html',{'products':products})
