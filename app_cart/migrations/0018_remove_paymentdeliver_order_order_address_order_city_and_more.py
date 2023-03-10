# Generated by Django 4.1.5 on 2023-01-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0017_complitedorder_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentdeliver',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='free_or_not',
            field=models.BooleanField(default=True, verbose_name='беслпатная доставка'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.BooleanField(default=True, verbose_name='оплата онлайн'),
        ),
        migrations.DeleteModel(
            name='OrderDeliver',
        ),
        migrations.DeleteModel(
            name='PaymentDeliver',
        ),
    ]
