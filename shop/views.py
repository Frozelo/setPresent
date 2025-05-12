from django.http import Http404
from django.shortcuts import render, get_object_or_404

from shop.models import Product

def index(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('name')

        return render(request, 'shop/index.html', {'products': products})


