# Generated by Django 5.0.4 on 2024-04-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
