from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
   
    return render(request, 'auth/login.html')

def register(request):  
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully registered")     
    else:
        form=UserCreationForm()

    return render(request, 'auth/register.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('login')  # Redirect to a success page.  # Create your views

def change_password(request):
    cp=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        cp=PasswordChangeForm(user=request.user,data=request.POST)
        if cp.is_valid():
            cp.save()
            return redirect('login')
    return render(request,"auth/change_password.html",{"cp":cp})
   