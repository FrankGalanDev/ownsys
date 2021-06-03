from django.shortcuts import render, redirect
from backoffice.models import User
from django.templatetags.static import static
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from backoffice.forms import CategTaskForm
from backoffice.models import CategTask
from django.core.paginator import Paginator


# Create your views here.

class CategTaskList(LoginRequiredMixin, ListView):
    model = CategTask
    paginate_by = 10
    template_name = 'categtasks/all_categtasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Task Category List'
        context['table_subtittle'] = 'All task categories List'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategTaskCreate(LoginRequiredMixin, CreateView):
    model = CategTask
    form_class = CategTaskForm
    template_name = 'categtasks/new_categtask.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Task category forms'
        context['table_tittle'] = 'New task category'
        context['table_subtittle'] = 'Add here your new task categories'
        context['action'] = 'add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_categtask')


class CategTaskUpdate(LoginRequiredMixin, UpdateView):
    model = CategTask
    form_class = CategTaskForm
    template_name = 'categtasks/update_categtask.html'
    success_url = reverse_lazy('all_categtask')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Category Task Forms'
        context['table_tittle'] = 'Edit Task Category'
        context['table_subtittle'] = 'Modify here your  task category'
        context['action'] = 'edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategTaskDelete(LoginRequiredMixin, DeleteView):
    model = CategTask
    template_name = 'brands/delete_categtask.html'
    success_url = reverse_lazy('all_categtask')


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tittle'] = 'Category Task Forms'
            context['table_tittle'] = 'Delete Category Task Form'
            context['table_subtittle'] = 'Delete here your category task'
            return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
