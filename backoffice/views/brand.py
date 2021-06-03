from django.shortcuts import render, redirect
from backoffice.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators  import method_decorator
#from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from backoffice.forms import BrandForm
from backoffice.models import Brand
from django.core.paginator import Paginator

 
# Create your views here.

class BrandList(LoginRequiredMixin, ListView):
    model = Brand
    paginate_by = 10
    template_name = 'brands/all_brands.html'
 
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Brand List'
        context['table_subtittle'] = 'All brands'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brands/new_brand.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Brand Forms'
        context['table_tittle'] = 'New Brand'
        context['table_subtittle'] = 'Add here your new brand'
        context['action'] ='add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_brand')


class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brands/update_brand.html'
    success_url = reverse_lazy('all_brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Brand Forms'
        context['table_tittle'] = 'Edit Brand'
        context['table_subtittle'] = 'Modify here your brand'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BrandDelete(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brands/delete_brand.html'
    success_url = reverse_lazy('all_brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Brand Forms'
        context['table_tittle'] = 'Delete Brand Form'
        context['table_subtittle'] = 'Delete here your brand'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
