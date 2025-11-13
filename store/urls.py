from  django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),  
    path('category/<str:category_slug>/', views.store, name='productos_por_categoria')

    # path('<str:category_slug>/', views.store, name='products-category'),
    ]