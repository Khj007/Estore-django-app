from django.urls import path
from .views.home import Index
from .views.login import Login,userlogout,adminlogin,adminlogout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import Orders
from .views.products import *
from .views.adminhome import Ahome
from .middlewares.auth import auth_middleware

urlpatterns = [
    # for user only
    path('',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('ulogin',Login.as_view(),name='ulogin'),
    path('logout',userlogout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='check-out'),
    path('orders',auth_middleware(Orders.as_view()),name='orders'),
    # for admin only
    path('alogin',adminlogin,name='alogin'),
    path('alogout',adminlogout,name='alogout'),
    path('home',Ahome,name='home'),
    path('addproduct',addProduct,name='addproduct'),
    path('product',showProducts,name='product'),
    path('remove/<int:pid>',destroyProduct,name='remove'),
    path('edit/<int:pid>',editProduct,name='edit'),
    path('updateproduct/<int:pid>',updateproduct,name='updateproduct'),
    path('productdata/<str:id>',productdetail,name='productdata'),
]
