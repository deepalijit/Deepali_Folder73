from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.

def signUpView(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    template_name='Accounts/signup.html'
    context={'form':form}
    return render(request,template_name,context)

def signInView(request):
    if request.method=='POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        #print(u,p)
        if user is not None:
            #print('correct credentials')
            login(request,user)
            return redirect('show-products')
        else:
            print('wrong credentials')
            messages.error(request,'Invalid Credentials')

    template_name = 'Accounts/signin.html'
    context={}
    return render(request,template_name,context)

def signOutView(request):
    logout(request)
    return redirect('signin')