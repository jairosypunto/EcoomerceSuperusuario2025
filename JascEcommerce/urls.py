
from django.contrib import admin
from django.urls import include, path

from JascEcommerce import settings
from .import views
from django.conf.urls.static import static #para imagenes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('usuario.urls')), #ruta para la aplicacion usuario
    path('', views.inicio, name="inicio"),
    path('',include("home.urls")),
    path('store/', include('store.urls')),
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT) #para imagenes
