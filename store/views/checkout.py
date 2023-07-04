from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
#class based view login
class Checkout(View)   :
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_By_Id(list(cart.keys()))

        for product in products:
            order=Order(customer=Customer(id=customer),
                        product=product,
                        price=product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.placeOrder()
        request.session['cart']={}    
        return redirect('cart')
