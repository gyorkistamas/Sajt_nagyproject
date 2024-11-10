from datetime import date
from hashlib import sha256
from math import prod
from re import template
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin as LoginReq
#from .models import Product, Cart, Order, OrderItem, Promo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.

#class ProfileView(LoginReq, TemplateView):
#    template_name = 'accounts/profile.html'

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def payment(request):
    return render(request, 'payment.html')

def items(request):
    Items:dict = {
        0: {
            "Name":"Termék neve",           
            "Description":"Rövid termék leírás",
            "Price":"11111",
            "Stock":"11"            
        },       
    }
    for i in range(1,30):
        Items[i] = {
            "ImagePath":"",
            "Name":f"Termék neve {i}",           
            "Description":"Rövid termék leírás",
            "Price":f"{i*2}",
            "Stock":f"{i}"  
        }
    return render(request, "items.html", {"Items":Items})
