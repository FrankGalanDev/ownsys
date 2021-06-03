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
from backoffice.forms import CompanyForm
from backoffice.models import Company


# Create your views here.

class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'company/see_company.html'
 
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Company data'
        context['table_subtittle'] = 'My company data'
        return context
    
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/create_company.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Company Forms'
        context['table_tittle'] = 'New company'
        context['table_subtittle'] = 'Add here your new company'
        context['action'] ='add'
        return context

    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('company_data')


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/update_company.html'
    success_url = reverse_lazy('company_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'company Forms'
        context['table_tittle'] = 'Edit company'
        context['table_subtittle'] = 'Modify here your company'
        context['action'] ='edit'
        return context

    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

'''
class companyDelete(LoginRequiredMixin, DeleteView):
    model = company
    template_name = 'companys/delete_company.html'
    success_url = reverse_lazy('all_company')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'company Forms'
        context['table_tittle'] = 'Delete company Form'
        context['table_subtittle'] = 'Delete here your company'
        return context

    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
'''