from django.shortcuts import render,redirect
from django.views import View
from store.models.category import Category
from store.models.product import Product

def loadProducts(request):
    return render(request,'addproducts.html')

def addProduct(request):
     if request.method == 'POST':
        vname=request.POST.get('name')
        vprice=request.POST.get('price')
        vdescription=request.POST.get('description')
        vcategory=request.POST.get('categery')
        category=Category.objects.all().filter(category=vcategory)
        print(vcategory)
        vimage=request.POST.get('image')
        obj=Product(name=vname,price=vprice,description=vdescription,category=category,image=vimage)
        obj.save()
        # cat=Category(category=vcategory)
        # print(vcategory)
        # cat.save()
        return redirect('/product')
     else:
        return render(request,'addproducts.html')

def showProducts(request):
    products=Product.objects.all()
    category=Category.objects.all()
    return render(request,'products.html',{'products':products,'category':category})

def productdetail(request,id):
    prod=Product.objects.filter(id=id).first()

    context={
        'prod':prod,
    }
    return render (request,'singleproduct.html',context)

def destroyProduct(request,pid):  
     stdobj=Product.objects.get(id=pid)
     stdobj.delete()
     return redirect('/product')

def editProduct(request,pid,cid):
    obj=Product.objects.get(id=pid)
    cat=Product.objects.get(id=cid)
    return render(request, "editdata.html",{'data':obj, 'cat':cat})  

def updateproduct(request,pid,cid):
    obj=Product.objects.get(id=pid)
    cat=Category.objects.get(id=cid)
    if request.method == 'POST':
        vname=request.POST.get('name')
        vprice=request.POST.get('price')
        vdescription=request.POST.get('description')
        vcategory=request.POST.get('categery')
        vimage=request.POST.get('image')
        obj.name=vname
        obj.price=vprice
        obj.description=vdescription
        cat.category=vcategory
        obj.image=vimage
        obj.save()
        return redirect('/product')
