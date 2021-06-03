from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import SectionForm
from backoffice.models import Section
from django.core.paginator import Paginator



# Create your views here.

class SectionList(ListView):
    model = Section
    paginate_by = 10
    template_name = 'sections/all_sections.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Section List'
        context['table_subtittle'] = 'all_section'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SectionCreate(CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'sections/new_section.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Sections Forms'
        context['table_tittle'] = 'New Section'
        context['table_subtittle'] = 'Add here your new sections'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('all_section')


class SectionUpdate(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'sections/section_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Section Forms'
        context['table_tittle'] = 'Edit Section'
        context['table_subtittle'] = 'Modify here your  Section'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SectionDelete(DeleteView):
    model = Section
    template_name = 'sections/delete_section.html'
    success_url = reverse_lazy('all_section')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Section Forms'
        context['table_tittle'] = 'Delete Section'
        context['table_subtittle'] = 'Delete here your section'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)