from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import PlatformForm
from backoffice.models import Platform
from django.core.paginator import Paginator


# Create your views here.

class PlatformList(LoginRequiredMixin, ListView):
    model = Platform
    paginate_by = 10
    template_name = 'platforms/all_platforms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'platform List'
        context['table_subtittle'] = 'All platforms'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PlatformCreate(CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'platforms/new_platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Platform Forms'
        context['table_tittle'] = 'New platform'
        context['table_subtittle'] = 'Add here your new platform'
        context['action'] ='add'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_platform')


class PlatformUpdate(UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'platforms/update_platform.html'
    success_url = reverse_lazy('all_platform')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Platform Forms'
        context['table_tittle'] = 'Edit platform'
        context['table_subtittle'] = 'Modify here your platform'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PlatformDelete(DeleteView):
    model = Platform
    template_name = 'platforms/delete_platform.html'
    success_url = reverse_lazy('all_platform')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Platform Forms'
        context['table_tittle'] = 'Delete platform Form'
        context['table_subtittle'] = 'Delete here your platform'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

