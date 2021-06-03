from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import TaskForm
from backoffice.models import Task
from django.core.paginator import Paginator



# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 10
    template_name = 'tasks/all_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'task List'
        context['table_subtittle'] = 'All tasks'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/new_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Tasks Forms'
        context['table_tittle'] = 'New task'
        context['table_subtittle'] = 'Add here your new task'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_task')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/all_tasks.html'
    success_url = reverse_lazy('all_task')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Task Forms'
        context['table_tittle'] = 'Edit task'
        context['table_subtittle'] = 'Modify here your task'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('all_task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Task Forms'
        context['table_tittle'] = 'Delete task Form'
        context['table_subtittle'] = 'Delete here your task'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

