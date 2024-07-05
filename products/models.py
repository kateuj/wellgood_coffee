from django.db import models
from django.db.models import CharField


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_variants = models.BooleanField(default=False, null=False, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Variant(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, blank=True)
    size = models.CharField(max_length=254, default=False, null=True, blank=True)
    grind = models.CharField(max_length=254, default=False, null=True, blank=True)
    roast = models.CharField(max_length=254, default=False, null=True, blank=True)
    flavour = models.CharField(max_length=254, default=False, null=True, blank=True)
    flavour_notes = CharField(max_length=254, default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_count = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name