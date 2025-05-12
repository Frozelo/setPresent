from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Cart, CartItem


def index(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'shop/index.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user_id=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart_id=cart, product_id=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def view_cart(request):
    cart = get_object_or_404(Cart, user_id=request.user)
    cart_items = CartItem.objects.filter(cart_id=cart)
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items})

