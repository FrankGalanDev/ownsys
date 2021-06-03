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
from backoffice.forms import DocumtForm
from backoffice.models import Documt
from django.core.paginator import Paginator



# Create your views here.

class DocumtList(LoginRequiredMixin, ListView):
    model = Documt
    paginate_by = 10
    template_name = 'documts/all_documts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Document List'
        context['table_subtittle'] = 'All documents'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DocumtCreate(LoginRequiredMixin, CreateView):
    model = Documt
    form_class = DocumtForm
    template_name = 'documts/new_documt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Document Forms'
        context['table_tittle'] = 'New Document'
        context['table_subtittle'] = 'Add here your new documents'
        context['action'] ='add'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_documt')


class DocumtUpdate(LoginRequiredMixin, UpdateView):
    model = Documt
    form_class = DocumtForm
    template_name = 'documts/update_documt.html'
    success_url = reverse_lazy('all_documt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'document Forms'
        context['table_tittle'] = 'Edit document'
        context['table_subtittle'] = 'Modify here your document'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DocumtDelete(LoginRequiredMixin, DeleteView):
    model = Documt
    template_name = 'documts/delete_documt.html'
    success_url = reverse_lazy('all_documt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Document Forms'
        context['table_tittle'] = 'Delete document Form'
        context['table_subtittle'] = 'Delete here your document'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)  
