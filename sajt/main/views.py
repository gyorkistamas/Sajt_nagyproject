from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin as LoginReq
#from .models import Product, Cart, Order, OrderItem, Promo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from cart.cart import Cart
from cart.models import Product
from datetime import timedelta, timezone
from django.conf import settings
# Create your views here.

#class ProfileView(LoginReq, TemplateView):
#    template_name = 'accounts/profile.html'

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html', {"contact_data": settings.CONTACTS})

def payment(request):
    return render(request, 'payment.html')

def items(request):
    Items:dict = {}
    for i in range(1,30):
        Items[i] = {
            "ImagePath":"",
            "filter":["",""],
            "Name":f"Termék neve {i}",           
            "Description":"Rövid termék leírás",
            "Price":f"{i*2}",
            "Stock":f"{i}"  
        }        
    return render(request, "items.html", {"Items":Items})
# TODO: Item editor

@require_POST
def add_to_cart(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    cart.add(get_object_or_404(Product, id=product_id), quantity)
    return redirect('items')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart_detail')