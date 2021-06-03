from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from backoffice.forms import ItemForm
from backoffice.models import Item
from django.core.paginator import Paginator



# Create your views here.

class ItemList(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 5
    template_name = 'items/all_items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Item List'
        context['table_subtittle'] = 'All items'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ItemByList(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 20
    template_name = 'items/all_items_by_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Item List'
        context['table_subtittle'] = 'All items'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)    

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/new_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Item Forms'
        context['table_tittle'] = 'New item'
        context['table_subtittle'] = 'Add here your new item'
        context['action'] ='add'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('all_item')


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/update_items.html'
    success_url = reverse_lazy('all_item')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Item Forms'
        context['table_tittle'] = 'Edit item'
        context['table_subtittle'] = 'Modify here your item'
        context['action'] ='edit'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'items/delete_item.html'
    success_url = reverse_lazy('all_item')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Item Forms'
        context['table_tittle'] = 'Delete item Form'
        context['table_subtittle'] = 'Delete here your item'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

