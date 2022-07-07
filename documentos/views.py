from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'pertence']

    def form_valid(self, form):
        obj = form.save()
        documento = obj
        documento.save()
        return super(DocumentoCreate, self).form_valid(form)


class DocumentoEdit(UpdateView):
    model = Documento
    fields = ['descricao', 'pertence']


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_funcionarios')


class DocumentosList(ListView):
    model = Documento

    def get_queryset(self):
        return Documento.objects.filter()


