from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from user.forms import RegistrationForm, LoginForm, ProfileForm
from shop.forms import OrderForm

from shop.models import Product, Cart, CartItem, Order, OrderItem


def index(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'shop/index.html', {'products': products})


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'shop/product_detail.html', {'product': product})


@login_required(login_url='auth')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(user_id=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart_id=cart, product_id=product, defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required(login_url='auth')
def view_cart(request):
    cart = get_object_or_404(Cart, user_id=request.user)
    cart_items = CartItem.objects.filter(cart_id=cart)
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items})


@login_required(login_url='auth')
def checkout(request):
    cart = get_object_or_404(Cart, user_id=request.user)
    cart_items = CartItem.objects.filter(cart_id=cart)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid() and cart_items.exists():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user_id = request.user
            order.save()
            for item in cart_items:
                OrderItem.objects.create(
                    order_id=order,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.product_id.price,
                )
            cart_items.delete()
            return redirect('catalog')
    else:
        form = OrderForm()

    return render(
        request,
        'shop/checkout.html',
        {'cart_items': cart_items, 'form': form},
    )


# Главная страница
def main_page(request):
    return render(request, "mainpage.html")


# Каталог
def catalog(request):
    products = Product.objects.all().order_by('name')
    return render(request, "catalog2.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recommended = (
        Product.objects.filter(category=product.category)
        .exclude(id=product.id)
        .order_by("?")[:5]
    )
    return render(
        request,
        "product2.html",
        {"product2": product, "recommended": recommended},
    )


def auth(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("catalog")
    else:
        form = LoginForm()
    return render(request, "auth.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user_id=user)
            login(request, user)
            return redirect("catalog")
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})


# Линый кабинет
def profile(request):
    if not request.user.is_authenticated:
        return redirect("auth")

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user_id=request.user)
        .prefetch_related("orderitem_set")
        .order_by("-order_date")
    )
    return render(request, "profile.html", {"form": form, "orders": orders})


def consturcot(request):
    return render(request, "constructor.html")


# Корзина
def cart(request):
    return render(request, "cart.html")


def favourites(request):
    return render(request, "favourites.html")
