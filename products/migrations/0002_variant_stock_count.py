# Generated by Django 5.0.6 on 2024-06-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='stock_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
