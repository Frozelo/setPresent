from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def str(self):
        return self.name


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey('Cart', on_delete=models.PROTECT)
    # One product can appear in many cart items, so use ForeignKey instead of
    # OneToOneField to avoid unique constraint issues when different users add
    # the same product to their carts.
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    user_comment = models.TextField(blank=True)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
