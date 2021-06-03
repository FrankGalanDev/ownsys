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
from backoffice.forms import CategDocForm
from backoffice.models import CategDoc
from django.core.paginator import Paginator


# Create your views here.

class CategDocList(LoginRequiredMixin, ListView):
    model = CategDoc
    paginate_by = 10
    template_name = 'categdocs/all_categdocs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Documents Category List'
        context['table_subtittle'] = 'All document categories list'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategDocCreate(LoginRequiredMixin, CreateView):
    model = CategDoc
    form_class = CategDocForm
    template_name = 'categdocs/new_categdoc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Document category Forms'
        context['table_tittle'] = 'New Document category'
        context['table_subtittle'] = 'Add here your new document categories'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_categdoc')


class CategDocUpdate(LoginRequiredMixin, UpdateView):
    model = CategDoc
    form_class = CategDocForm
    template_name = 'categdocs/update_categdoc.html'
    success_url = reverse_lazy('all_categdoc')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Docs Forms'
        context['table_tittle'] = 'Edit Document Category'
        context['table_subtittle'] = 'Modify here your  document category'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategDocDelete(LoginRequiredMixin, DeleteView):
    model = CategDoc
    template_name = 'categdocs/delete_categdoc.html'
    success_url = reverse_lazy('all_categdoc')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Document Forms'
        context['table_tittle'] = 'Delete  Document Category Form'
        context['table_subtittle'] = 'Delete here your document category'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
