from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return super(EmpresaCreate, self).form_valid(form)


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']


class EmpresaDelete(DeleteView):
    model = Empresa
    success_url = reverse_lazy('list_funcionarios')


class EmpresasList(ListView):
    model = Empresa

    def get_queryset(self):
        #empresa_logada = self.request.user.funcionario.empresa
        return Empresa.objects.filter()


