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
from backoffice.forms import CourierForm
from backoffice.models import Courier
from django.core.paginator import Paginator


# Create your views here.
  
class CourierList(LoginRequiredMixin, ListView):
    model = Courier
    paginate_by = 10
    template_name = 'couriers/all_couriers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Couriers List'
        context['table_subtittle'] = 'All couriers'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CourierCreate(LoginRequiredMixin, CreateView):
    model = Courier
    form_class = CourierForm
    template_name = 'couriers/new_courier.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Courier Forms'
        context['table_tittle'] = 'New courier'
        context['table_subtittle'] = 'Add here your new courier'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_courier')


class CourierUpdate(LoginRequiredMixin, UpdateView):
    model = Courier
    form_class = CourierForm
    template_name = 'couriers/update_courier.html'
    success_url = 'couriers/all_couriers.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Courier Forms'
        context['table_tittle'] = 'Edit courier'
        context['table_subtittle'] = 'Modify here your courier'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CourierDelete(DeleteView):
    model = Courier
    template_name = 'couriers/delete_courier.html'
    success_url = reverse_lazy('all_courier')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Courier Forms'
        context['table_tittle'] = 'Delete Courier Form'
        context['table_subtittle'] = 'Delete here your courier'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
