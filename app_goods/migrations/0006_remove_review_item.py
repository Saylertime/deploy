# Generated by Django 4.1.5 on 2023-01-19 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0005_seller_item_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='item',
        ),
    ]