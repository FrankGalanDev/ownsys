from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import ReturnedForm
from backoffice.models import Returned
from django.core.paginator import Paginator
 


# Create your views here.

class ReturnedList(LoginRequiredMixin, ListView):
    model = Returned
    paginate_by = 10
    template_name = 'returneds/all_returneds.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Returned Item List'
        context['table_subtittle'] = 'All returneds'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ReturnedCreate(LoginRequiredMixin, CreateView):
    model = Returned
    form_class = ReturnedForm
    template_name = 'returneds/new_returned.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'returned Forms'
        context['table_tittle'] = 'New returned'
        context['table_subtittle'] = 'Add here your new returneds'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_returned')


class ReturnedUpdate(LoginRequiredMixin, UpdateView):
    model = Returned
    form_class = ReturnedForm
    template_name = 'returneds/update_returned.html'
    success_url = reverse_lazy('all_returned')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Returned Forms'
        context['table_tittle'] = 'Edit returned'
        context['table_subtittle'] = 'Modify here your returned'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ReturnedDelete(LoginRequiredMixin, DeleteView):
    model = Returned
    template_name = 'returneds/delete_returned.html'
    success_url = reverse_lazy('all_returned')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Returned Forms'
        context['table_tittle'] = 'Delete returned Form'
        context['table_subtittle'] = 'Delete here your returned'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
