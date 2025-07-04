# Generated by Django 5.2.3 on 2025-06-16 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_order_address_order_email_order_name_order_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="product_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="shop.product"
            ),
        ),
    ]
