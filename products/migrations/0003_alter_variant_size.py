# Generated by Django 5.0.6 on 2024-06-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variant_stock_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='size',
            field=models.CharField(blank=True, default=False, max_length=254, null=True),
        ),
    ]
