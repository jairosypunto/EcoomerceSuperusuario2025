from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    nombre_categoria = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    descripcion = models.TextField(max_length=200, default='Sin descripción')
    
    def __str__(self):
        return self.nombre_categoria
    
    def get_url(self):
       return reverse('store:productos_por_categoria', args=[self.slug])

 