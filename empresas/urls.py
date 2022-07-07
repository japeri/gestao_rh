from django.urls import path
from .views import (
    EmpresasList,
    EmpresaEdit,
    EmpresaDelete,
    EmpresaCreate
)


urlpatterns = [
    path('', EmpresasList.as_view(), name='list_empresas'),
    path('novo/', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='update_empresa'),
    path('delete/<int:pk>/', EmpresaDelete.as_view(), name='delete_empresa'),
]
