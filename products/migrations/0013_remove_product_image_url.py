# Generated by Django 5.0.6 on 2024-07-23 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
