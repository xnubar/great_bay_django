from django.shortcuts import render
from django.http import HttpResponse 
from .models import Item
import json


def get_products(request):
    print('salam')
    if request.is_ajax():
        products = json.dumps(list(Item.objects.values('id', 'name', 'status', 'start_bid')))
        products_json = json.dumps(products)
        print(products_json)
        return HttpResponse(products_json, content_type="application/json")
        