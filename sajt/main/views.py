from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin as LoginReq
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from cart.cart import Cart
from itemManager.models import Product
from django.conf import settings
from random import randint

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html', {"contact_data": settings.CONTACTS})
@login_required
def payment(request):
    return render(request, 'payment.html')

def items(request, filter=None):  
    products: list[Product] = []
    if not filter:      
        products = Product.objects.all()
    return render(request, "items.html", { "Items":products, 'count': len(products) })

@login_required
@require_POST
def add_to_cart(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    cart.add(get_object_or_404(Product, id=product_id), quantity)
    return redirect('items')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})
@login_required
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart_detail')