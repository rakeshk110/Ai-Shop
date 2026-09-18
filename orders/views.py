from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order

@login_required
def place_order(request,product_id):
    product = Product.objects.get(id=product_id)
    quantity = 1
    total = product.price * quantity

    Order.objects.create(
        user=request.user,
        product=product,
        quantity=quantity,
        price=product.price,
        total=total
    )
    return redirect("orders")

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request,"orders/orders.html",{'orders':orders})