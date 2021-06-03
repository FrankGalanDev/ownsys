from django.shortcuts import render, redirect
from backoffice.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from backoffice.forms import CategItemForm
from backoffice.models import CategItem
from django.core.paginator import Paginator


# Create your views here.

class CategItemList(LoginRequiredMixin, ListView):
    model = CategItem
    paginate_by = 10
    template_name = 'categitems/all_categitems.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Item Category List'
        context['table_subtittle'] = 'All item categories List'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategItemCreate(LoginRequiredMixin, CreateView):
    model = CategItem
    form_class = CategItemForm
    template_name = 'categitems/new_categitem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Item category Forms'
        context['table_tittle'] = 'New Item category'
        context['table_subtittle'] = 'Add here your new item categories'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('all_categitem')


class CategItemUpdate(LoginRequiredMixin, UpdateView):
    model = CategItem
    form_class = CategItemForm
    template_name = 'categitems/update_categitem.html'
    success_url =reverse_lazy ('all_categitem')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Item Forms'
        context['table_tittle'] = 'Edit Category'
        context['table_subtittle'] = 'Modify here your  item category'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



class CategItemDelete(LoginRequiredMixin, DeleteView):
    model = CategItem
    template_name= 'categitems/delete_categitem.html'
    success_url = reverse_lazy('all_categitem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Product Category Forms'
        context['table_tittle'] = 'Delete category product Form'
        context['table_subtittle'] = 'Delete here your product category'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

