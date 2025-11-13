from django.shortcuts import get_object_or_404, render
from .models import Product
from categorias.models import Category
# Create your views here.
def store(request,category_slug=None):
    category = None
    products = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(is_available=True) 
        counter_products = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        counter_products = products.count()
    context={
        'all_products': products,
        'counter_products': counter_products,
    }
    return render(request, 'store/tienda.html',context=context)