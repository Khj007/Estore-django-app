from django.shortcuts import render,redirect
from django.views import View

def Ahome(request):
    return render(request,'adminbase.html')

    # if request.user.is_authenticated:
    #     return render(request,'adminbase.html')
    # else:
    #     return redirect('/alogin')