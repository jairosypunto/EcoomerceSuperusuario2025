from django.contrib import admin

from store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'stock', 'is_available', 'category', 'date_register', 'date_update')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('cost', 'stock', 'is_available')
    ordering = ('-date_register',)
admin.site.register(Product, ProductAdmin)