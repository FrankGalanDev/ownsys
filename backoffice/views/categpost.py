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
from backoffice.forms import CategPostForm
from backoffice.models import CategPost
from django.core.paginator import Paginator


# Create your views here.

class CategPostList(LoginRequiredMixin, ListView):
    model = CategPost
    paginate_by = 10
    template_name = 'categposts/all_categposts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Post Category List'
        context['table_subtittle'] = 'All Post categories list'
        return context


class CategPostCreate(LoginRequiredMixin, CreateView):
    model = CategPost
    form_class = CategPostForm
    template_name = 'categposts/new_categpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Post category Forms'
        context['table_tittle'] = 'New post category'
        context['table_subtittle'] = 'Add here your new post categories'
        context['action'] ='add'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_categpost')


class CategPostUpdate(LoginRequiredMixin, UpdateView):
    model = CategPost
    form_class = CategPostForm
    template_name = 'categposts/update_categpost.html'
    success_url = reverse_lazy('all_categpost')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Post Forms'
        context['table_tittle'] = 'Edit Post Category'
        context['table_subtittle'] = 'Modify here your  post category'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategPostDelete(LoginRequiredMixin, DeleteView):
    model = CategPost
    template_name = 'categposts/delete_categpost.html'
    success_url = reverse_lazy('all_categpost')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Post Forms'
        context['table_tittle'] = 'Edit  Category Post'
        context['table_subtittle'] = 'Delete here your  post category'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
