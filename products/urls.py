from django.urls import path
from .views import *

urlpatterns = [
    path("",home, name="home"),
    path("category/<int:category_id>/", category_products, name="category_products"),
    path("create_product/", product_create, name="product_create"),
    path("list/",product_list, name="list_product"),
    path("<int:product_id>/update/", product_update, name="product_update"),
    path("<int:product_id>/delete/",product_delete, name="product_delete"),
    path("cart/add/<int:product_id>/",add_to_cart, name="add_to_cart"),
    path("cart/",cart,name="cart"),
    path("cart/increase/<int:product_id>/", increase_quantity, name="increase_quantity"),
    path("cart/decrease/<int:product_id>/", decrease_quantity, name="decrease_quantity"),
    path("cart/remove/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("product/<int:product_id>/",product_detail,name="product_detail"),

    
]