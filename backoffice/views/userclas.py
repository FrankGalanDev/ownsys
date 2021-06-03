from django.shortcuts import render
#from django.contrib.auth.models import User
from backoffice.models import UserClas
from django.utils.text import slugify
from django.templatetags.static import static
from django.views.generic import ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from backoffice.forms import UserClasForm

# Create your views here.



class UserClasList(LoginRequiredMixin,ListView):
    model = UserClas
    template_name = "usersclas/all_usersclas.html"


    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['clas_name'] = 'Userclas List'
    	context['description'] = 'Userclas List'
    	return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserClasCreate(LoginRequiredMixin, CreateView):
    model = UserClas
    form_class = UserClasForm
    template_name = 'usersclas/new_userclas.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'User Class Forms'
        context['table_tittle'] = 'New User class'
        context['table_subtittle'] = 'Add here your new class for users'
        context['action'] ='add'

        return context
        
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_usersclas')


class UserClasUpdate(LoginRequiredMixin, UpdateView):
    model = UserClas
    form_class = UserClasForm
    template_name = 'usersclas/update_userclas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Userclas Forms'
        context['table_tittle'] = 'Edit userclas'
        context['table_subtittle'] = 'Modify here your userclas'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserClasDelete(LoginRequiredMixin, DeleteView):
    model = UserClas
    success_url = reverse_lazy('all_userclas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Userclas Forms'
        context['table_tittle'] = 'Edit userclas'
        context['table_subtittle'] = 'Modify here your userclas'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)