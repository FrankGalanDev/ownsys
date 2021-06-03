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
from backoffice.forms import LevelForm
from backoffice.models import Level
from django.core.paginator import Paginator


# Create your views here.

class LevelList(LoginRequiredMixin, ListView):
    model = Level
    paginate_by = 10
    template_name = 'levels/all_levels.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Level List'
        context['table_subtittle'] = 'All levels'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class LevelCreate(LoginRequiredMixin, CreateView):
    model = Level
    form_class = LevelForm
    template_name = 'levels/new_level.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Level Forms'
        context['table_tittle'] = 'New level'
        context['table_subtittle'] = 'Add here your new level'
        context['action'] ='add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_level')


class LevelUpdate(LoginRequiredMixin, UpdateView):
    model = Level
    form_class = LevelForm
    template_name = 'levels/update_level.html'
    success_url = reverse_lazy('all_level')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Level Forms'
        context['table_tittle'] = 'Edit level'
        context['table_subtittle'] = 'Modify here your level'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LevelDelete(LoginRequiredMixin, DeleteView):
    model = Level
    template_name = 'levels/delete_level.html'
    success_url = reverse_lazy('all_level')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Level Forms'
        context['table_tittle'] = 'Delete level Form'
        context['table_subtittle'] = 'Delete here your level'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
