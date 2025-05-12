from django.contrib import admin

from shop.models import Category, Product, OrderItem, Order, CartItem, Cart

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

