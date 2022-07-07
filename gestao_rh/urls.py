from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('documentos/', include('documentos.urls')),
    path('empresa/', include('empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
