from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Cart, CartItem, Order, OrderItem


def index(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'shop/index.html', {'products': products})


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'shop/product_detail.html', {'product': product})


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


def checkout(request):
    cart = get_object_or_404(Cart, user_id=request.user)
    print(cart)
    cart_items = CartItem.objects.filter(cart_id=cart)

    if cart_items.exists():
        order = Order.objects.create(user_id=request.user, user_comment=request.POST.get('comment', ''))
        for item in cart_items:
            OrderItem.objects.create(order_id=order, product_id=item.product_id, quantity=item.quantity,
                                     price=item.product_id.price)
        cart_items.delete()
        return redirect('shop')

    return render(request, 'shop/checkout.html')


# Главная страница
def main_page(request):
    return render(request, "mainpage.html")


# Каталог
def catalog(request):
    return render(request, "catalog.html")


def product_detail(request, product_id):
    return render(request, "product_detail.html")


def auth(request):
    return render(request, "auth.html")


def registration(request):
    return render(request, "registration.html")


# Линый кабинет
def profile(request):
    return render(request, "profile.html")


# Корзина
def cart(request):
    return render(request, "cart.html")

def favourites(request):
    return render(request, "favourites.html")