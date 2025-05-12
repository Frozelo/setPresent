from django.urls import path

from shop.views import index, product_detail, add_to_cart, view_cart, checkout

urlpatterns = [
    path('', index, name='shop'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout')
]
