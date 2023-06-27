from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'Home.html');
def loginpage(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('Password') 
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('home');
        else:
            return HttpResponse ("username and pass is incorrect")
    return render (request,'login.html')
