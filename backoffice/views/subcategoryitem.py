from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse, reverse_lazy
from backoffice.forms import SubcategoryItemForm
from backoffice.models import SubcategoryItem
from django.core.paginator import Paginator



# Create your views here.

class SubcategoryItemList(LoginRequiredMixin, ListView):
    model = SubcategoryItem
    paginate_by = 10
    template_name = 'subcategoryitems/all_subcategoryitems.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Item Category List'
        context['table_subtittle'] = 'All item categories List'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class SubcategoryItemCreate(LoginRequiredMixin, CreateView):
    model = SubcategoryItem
    form_class = SubcategoryItemForm
    template_name = 'subcategoryitems/new_subcategoryitem.html'

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


class SubcategoryItemUpdate(LoginRequiredMixin, UpdateView):
    model = SubcategoryItem
    form_class = SubcategoryItemForm
    template_name = 'subcategoryitem/all_subcategoryitems.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Subcategory item Forms'
        context['table_tittle'] = 'Edit subcategory item'
        context['table_subtittle'] = 'Modify here your subcategory item'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SubcategoryItemDelete(LoginRequiredMixin, DeleteView):
    model = SubcategoryItem
    template_name = 'brands/delete_brand.html'
    success_url = reverse_lazy('all_subcategoryitem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Subcategory Forms'
        context['table_tittle'] = 'Delete subcategory Form'
        context['table_subtittle'] = 'Delete here your subcategory'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
