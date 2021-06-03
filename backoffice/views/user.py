from django.shortcuts import render
from backoffice.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.utils.text import slugify
from django.templatetags.static import static
from django.views.generic import ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import UserForm
from django.core.paginator import Paginator


# Create your views here.



class UserList(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 5
    template_name = "users/all_users.html"


    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['username'] = 'User List'
    	context['first_name'] = 'User List'
    	context['email_address'] = 'User List'
    	context['photouser'] = 'User List'   	
    	return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserByList(ListView):
    model = User
    paginate_by = 15
    template_name = "users/all_users_by_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'User List'
        context['first_name'] = 'User List'
        context['email_address'] = 'User List'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

 
class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/new_user.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'User Forms'
        context['table_tittle'] = 'New User'
        context['table_subtittle'] = 'Add here your new user'
        context['action'] ='add'

        return context
        
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_user')


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('all_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'User Forms'
        context['table_tittle'] = 'Edit user'
        context['table_subtittle'] = 'Modify here your user'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('all_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'User Forms'
        context['table_tittle'] = 'Edit user'
        context['table_subtittle'] = 'Modify here your user'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)




