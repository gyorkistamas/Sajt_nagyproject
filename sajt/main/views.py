from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin as LoginReq
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Cart, CartItems
from itemManager.models import Product
from django.conf import settings
from django.contrib import messages
from accounts.models import Orders, OrdersItems, CustomUser



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
def cart_detail(request):
    cart = Cart.objects.get(userId=request.user)
    if cart:
        if CartItems.objects.filter(cartId=cart.id).exists():
            _cart_items = CartItems.objects.filter(cartId=cart.id).all()
            cart_items = {}
            for item in _cart_items:
                temp_product = Product.objects.get(id=item.itemId.id)
                cart_items[item.itemId.id] = {
                    "id": item.id,
                    "cartId": item.cartId.id,
                    "product_id": item.itemId.id, 
                    "quantity": item.quantity,
                    "product_name": temp_product.name,
                    "product_price": temp_product.price,
                    "product_image": temp_product.image,
                    "product_category": temp_product.categoryId,
                    "product_stock": temp_product.stock,
                    "product_description": temp_product.description,
                    "total_price": temp_product.price * item.quantity
                }
            for key, item in cart_items.items():
                print("{}: {}".format(key, item))
            return render(request, 'cart_detail.html', {'cart': cart_items})
    else:
        messages = messages.error(request=request,messages="Cart not found!")
    return render(request, 'cart_detail.html', {'cart': cart_items})

@login_required
@require_POST
def add_to_cart(request):
    print(request.user.id)
    try:
        if request.method == "POST":
            print("In post cart add")
            cart = Cart.objects.get(userId=request.user.id)  
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity'))
            cart_item = CartItems.objects.filter(cartId=cart.id, itemId=product_id)
            if cart_item:
                cart_item.quantity += quantity
                print(f"[SUCCESS] Item successfully increased in cart by {quantity}, id: {product_id}") 
                cart_item.save()
                return redirect('items')
            else:
                cart_item = CartItems.objects.create(cartId=cart, itemId=Product.objects.get(id=product_id), quantity=quantity)
                cart_item.save()
                print(f"[SUCCESS] Item successfully added to cart, id: {product_id}")
    except Exception as e:
        print(f"[ERROR] Unexpected exception: {e}")
    return redirect('items')


@login_required
@require_POST
def cart_remove(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        cart = Cart.objects.get(userId=request.user.id)
        if cart:
            if CartItems.objects.filter(cart=cart, itemId=product_id).exists():
                cart_item = CartItems.objects.get(cart=cart, itemId=product_id)
                cart_item.delete()
                messages.success(request=request, message=f"Item successfully deleted! id:{product_id}")
            else:
                messages.error(request=request,message=f"Item not found in cart! id:{product_id}")
        else:
            messages.error(request=request,message=f"Cart not found! id:{product_id}")
    return redirect('cart_detail')

@login_required
@require_POST
def cart_increase_item(request, product_id):
    if request.method == "POST":
        cart = Cart.objects.get(userId=request.user.id)
        if cart:
            cart_item = CartItems.objects.get(cart=cart, itemId=product_id)
            if cart_item:
                cart_item.quantity += 1
            else:
                messages.error(request=request,message=f"Item not found in cart! id:{product_id}")
        else:
            messages.error(request=request,message=f"Cart not found! id:{product_id}")
    return redirect('cart_detail')

@login_required
@require_POST
def cart_decrease_item(request, product_id):
    if request.method == "POST":
        cart = Cart.objects.get(userId=request.user.id)
        if cart:
            cart_item = CartItems.objects.get(cart=cart, itemId=product_id)
            if cart_item:
                cart_item.quantity -= 1
            else:
                messages.error(request=request,message=f"Item not found in cart! id:{product_id}")
        else:
            messages.error(request=request,message=f"Cart not found! id:{product_id}")
    return redirect('cart_detail')

@login_required
def order_detail(request):
    try:
        order = Orders.objects.get(userId=request.user.id)
        if order:
            order_items = OrdersItems.objects.filter(order=order.id)
            if order_items:
                return render(request, 'order_details.html', {'order_items': order_items, 'isNew':False})
            else:
                messages.error(request, "Hiba történt!")
                return render(request, 'order_details.html', {'order_items': None, 'isNew':False})
        else:
            return render(request, 'order_details.html', {"order_items":None, 'isNew':True})
    except Exception as e:
        messages.error(request, e)
        return render(request, 'order_details.html', {"order_items":None, 'isNew':True})


                