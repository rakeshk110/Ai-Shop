from django.urls import path
from .views import *

urlpatterns = [
    path("place/<int:product_id>",place_order,name="place_order"),
    path("",orders,name="orders"),
]