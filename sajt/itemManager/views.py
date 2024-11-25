from django.shortcuts import render
from accounts.models import CustomUser
from models import Product, CreateProductQueue
from django.views.decorators.http import login_required
# Create your views here.

@login_required
def create_item_view(request):
    if request.method == "POST":
        userID = CustomUser.objects.get(username=request.POST.get("username"))
        product_id = request.POST.get("productID")
        category_id = request.POST.get("categoryID")
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        image_url = request.POST.get("image")        
        CreateProductQueue.objects.create(category_id=category_id, name=name, description=description, price=price, stock=stock, categoryId=category_id, image=image_url, status="PENDING")

@login_required
def filter_products(request, categoryId):
    products = Product.objects.filter(categoryId=categoryId)
    return render(request, "items.html", {"Items":products})
    
@login_required
def search_products(request, searchPhrase):
    pass