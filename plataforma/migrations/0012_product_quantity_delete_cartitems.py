# Generated by Django 5.0.4 on 2024-05-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_rename_product_cartitems_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
