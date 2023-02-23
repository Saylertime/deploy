# Generated by Django 4.1.5 on 2023-01-22 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0024_item_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_items', to='app_goods.subcategory', verbose_name='подкатегория'),
        ),
    ]