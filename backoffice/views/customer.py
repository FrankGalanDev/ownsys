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
from backoffice.forms import CustomerForm
from backoffice.models import Customer
from django.core.paginator import Paginator


 
# Create your views here.

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 10
    template_name = 'customers/all_customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Customer List'
        context['table_subtittle'] = 'All customers'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/new_customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Customer Forms'
        context['table_tittle'] = 'New customer'
        context['table_subtittle'] = 'Add here your new customer'
        context['action'] ='add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_customer')


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/update_customer.html'
    success_url = 'customers/all_customers.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Customer Forms'
        context['table_tittle'] = 'Edit customer'
        context['table_subtittle'] = 'Modify here your customer'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_url = reverse_lazy('all_customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Customer Forms'
        context['table_tittle'] = 'Delete customer Form'
        context['table_subtittle'] = 'Delete here your customer'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
