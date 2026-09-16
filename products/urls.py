from django.urls import path
from .views import *

urlpatterns = [
    path("home/",home, name="home"),
    path("category/<int:category_id>/", category_products, name="category_products"),
    path("create_product/", product_create, name="product_create"),
    path("list/",product_list, name="list_product"),
    path("/<int:product_id>/update/", product_update, name="product_update"),
    path("/<int:product_id>/delete/",product_delete, name="product_delete")
    
]