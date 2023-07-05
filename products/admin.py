from django.contrib import admin

from products.models import ProductCategory, Product, Basket



admin.site.register(ProductCategory)


@admin.register(Product) # отображение в админ-панели
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)
    extra = 1