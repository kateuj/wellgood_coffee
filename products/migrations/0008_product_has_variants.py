# Generated by Django 5.0.6 on 2024-07-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_variants',
            field=models.BooleanField(default=False),
        ),
    ]
