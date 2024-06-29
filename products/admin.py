from django.contrib import admin
from .models import Product, Category, Variant

# Register your models here.

class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product',
        'price',
        'grind',
        'roast',
        'flavour',
        'flavour_notes',
        'size',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'rating',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variant, VariantAdmin)