from django.urls import path
from .views import home,category_products

urlpatterns = [
    path("home/",home),
    path("category/<int:category_id>/", category_products,name="category_products")
    
]