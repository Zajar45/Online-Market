from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import item, category
from .forms import SignUpForm
from django.urls import reverse
from django.contrib import messages


def index(request):
    items = item.objects.filter(is_sold=False)[0:6]
    categories = category.objects.all()

    return render(request, 'core/index.html',{'items':items, 'categories':categories})

def contact(request):
    return render(request, 'core/contact.html',{})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "you have been registered successfuly..")
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, "you have been logged out..")

    return redirect(reverse('core:index'))

    