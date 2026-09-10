from django.shortcuts import render,get_object_or_404
from .models import Product,Category

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,"home.html",{
        "products":products,
        "categories": categories
        })

def category_products(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    products = Product.objects.filter(Category=category)
    categories = Category.objects.all()
    return render(request,"home.html",{
            "products":products,
            "categories": categories
            })

