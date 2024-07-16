from django.contrib import admin
from .models import Product, Category, Variant

# Register your models here.

class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product',
        'name',
        'price',
        'grind',
        'size',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'rating',
        'price',
        'image',
        'roast',
        'flavour_notes',
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