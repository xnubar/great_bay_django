from django.urls import path
from .views import *

urlpatterns = [
    path("getall/", get_products, name = "allproducts" ),
]