from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category,CartItem
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

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


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()

    return render(request,"products/product_form.html",{"form":form})

def product_list(request):
    products = Product.objects.all()
    return render(request,"products/product_list.html",{"products":products})


def product_update(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("list_product")
    else:
        form = ProductForm(instance=product)

    return render(request,"products/product_form.html",{"form":form})


def product_delete(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("list_product")
    return render(request,"products/product_confirm_delete.html",{"product":product})

#Cart
@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user,product=product)

    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect("home")


@login_required
def cart(request):
    cart_item = CartItem.objects.filter(user=request.user)
    total_price = 0

    for item in cart_item:
        total_price += item.product.price * item.quantity

    return render(request,"products/cart.html",{
        "cart_items":cart_item,
        "total_price":total_price})
