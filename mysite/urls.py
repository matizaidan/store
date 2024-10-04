from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),  # Incluir las URLs de la tienda
]
