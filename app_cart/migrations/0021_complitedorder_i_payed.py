# Generated by Django 4.1.5 on 2023-01-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0020_remove_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complitedorder',
            name='i_payed',
            field=models.BooleanField(null=True, verbose_name='платил со своей карты'),
        ),
    ]