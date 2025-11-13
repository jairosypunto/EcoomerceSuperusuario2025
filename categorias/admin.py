from django.contrib import admin
# Register your models here.
from .models import Category  # ✅
#admin.site.register(Categoria)
@admin.register(Category)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'slug', 'descripcion')
    prepopulated_fields = {'slug': ('nombre_categoria',)}
    search_fields = ('nombre_categoria', 'descripcion',)
    list_filter = ('nombre_categoria',)
    list_per_page = 2 