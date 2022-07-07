from django.db import models
from django.urls import reverse

from funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return str(self.pertence) + " - " + self.descricao

    def get_absolute_url(self):
        return reverse('home')
