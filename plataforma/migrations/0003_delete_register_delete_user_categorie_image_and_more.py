# Generated by Django 5.0.4 on 2024-04-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_rename_resources_categorie_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='categorie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/images/'),
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comments/images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/images/'),
        ),
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resources/images/'),
        ),
    ]