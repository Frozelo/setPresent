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
    product_id = models.OneToOneField('Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    user_comment = models.TextField()


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
