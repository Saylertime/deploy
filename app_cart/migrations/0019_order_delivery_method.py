# Generated by Django 4.1.5 on 2023-01-31 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0018_remove_paymentdeliver_order_order_address_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.BooleanField(default=False, verbose_name='экспресс-доставка'),
        ),
    ]
