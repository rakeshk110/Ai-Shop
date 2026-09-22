from django.contrib import admin
from .models import Category, Product,CartItem,UserActivity

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(UserActivity)