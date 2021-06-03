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
from backoffice.forms import InventoryForm
from backoffice.models import Inventory
from django.core.paginator import Paginator


# Create your views here.

class InventoryList(LoginRequiredMixin, ListView):
    model = Inventory
    paginate_by = 10
    template_name = 'inventory/all_inventories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Inventory Item List'
        context['table_subtittle'] = 'All inventories'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class InventoryCreate(LoginRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/new_inventory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Inventory Forms'
        context['table_tittle'] = 'New inventory'
        context['table_subtittle'] = 'Add here your new inventorys'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_inventory')


class InventoryUpdate(LoginRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/update_inventory.html'
    success_url = 'inventory/all_inventories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Inventory Forms'
        context['table_tittle'] = 'Edit inventory'
        context['table_subtittle'] = 'Modify here your inventory'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class InventoryDelete(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = "inventory/delete_inventory.html"
    success_url = reverse_lazy('all_inventory')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Inventory Forms'
        context['table_tittle'] = 'Delete inventory'
        context['table_subtittle'] = 'Delete here your inventory'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

