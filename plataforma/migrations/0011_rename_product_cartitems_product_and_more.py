# Generated by Django 5.0.4 on 2024-05-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0010_rename_cartitem_cartitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='Product',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]