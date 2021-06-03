from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from backoffice.forms import CurrencyForm
from backoffice.models import Currency
from django.core.paginator import Paginator



# Create your views here.

class CurrencyList(LoginRequiredMixin, ListView):
    model = Currency
    paginate_by = 10
    template_name = 'currencies/all_currencies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Currency List'
        context['table_subtittle'] = 'All currencies'
        return context


class CurrencyCreate(LoginRequiredMixin, CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currencies/new_currency.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Currency Forms'
        context['table_tittle'] = 'New currency'
        context['table_subtittle'] = 'Add here your new currencys'
        context['action'] ='add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_currency')


class CurrencyUpdate(LoginRequiredMixin, UpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currencies/update_currency.html'
    success_url = reverse_lazy('all_currency')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'currency Forms'
        context['table_tittle'] = 'Edit currency'
        context['table_subtittle'] = 'Modify here your currency'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CurrencyDelete(LoginRequiredMixin, DeleteView):
    model = Currency
    template_name = 'currencies/delete_currency.html'
    success_url = reverse_lazy('all_currency')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'currency Forms'
        context['table_tittle'] = 'Delete currency Form'
        context['table_subtittle'] = 'Delete here your currency'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
