# Generated by Django 5.0.4 on 2024-05-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0012_product_quantity_delete_cartitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
