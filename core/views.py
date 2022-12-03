from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# def login_page(request):
#     if request.method=='POST':
#         username= request.POST.get('username')
#         password =request.POST.get('password')
#         user =authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('index')
#         else:
#             messages.info(request,'username invalid')
#     return render(request,'login.html')
# def logout(request):
#     return redirect('login_page')
# def register(request):
#     form = UserCreationForm()
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_page')
#     context={'form':form}
#     return render(request,'register.html',context)
def index(request):
    tasks= Taks.objects.all()
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context ={ 'tasks':tasks,'form':form}
    return render(request, 'view_page.html',context)
def update_task(request,id):
    task = Taks.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method=='POST':
        form =TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request,'update.html',context)

def delete_taks(request,id):
    item = Taks.objects.get(id=id)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'delete.html',context)