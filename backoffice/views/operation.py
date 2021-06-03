from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import OperationForm
from backoffice.models import Operation
from django.core.paginator import Paginator


# Create your views here.

class OperationList(LoginRequiredMixin, ListView):
    model = Operation
    paginate_by = 10
    template_name = 'operations/all_operations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Operation List'
        context['table_subtittle'] = 'All operations'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OperationCreate(LoginRequiredMixin, CreateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operations/new_operation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Operation Forms'
        context['table_tittle'] = 'New operation'
        context['table_subtittle'] = 'Add here your new operation'
        context['action'] ='add'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_operation')


class OperationUpdate(LoginRequiredMixin, UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operations/update_operation.html'
    success_url = reverse_lazy('all_operation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Operation Forms'
        context['table_tittle'] = 'Edit operation'
        context['table_subtittle'] = 'Modify here your operation'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OperationDelete(LoginRequiredMixin, DeleteView):
    model = Operation
    template_name = 'operations/delete_operation.html'
    success_url = reverse_lazy('all_operation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Operation Forms'
        context['table_tittle'] = 'Delete operation Form'
        context['table_subtittle'] = 'Delete here your operation'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

