from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import CommentForm
from backoffice.models import Comment
from django.core.paginator import Paginator

 

# Create your views here.

class CommentList(LoginRequiredMixin, ListView):
    model = Comment
    paginate_by = 10
    template_name = 'comments/all_comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'comment List'
        context['table_subtittle'] = 'All comments'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/new_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Comment Forms'
        context['table_tittle'] = 'New comment'
        context['table_subtittle'] = 'Add here your new comment'
        context['action'] ='add'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_comment')


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/update_comment.html'
    success_url = reverse_lazy('all_comment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Comment Forms'
        context['table_tittle'] = 'Edit Comment'
        context['table_subtittle'] = 'Modify here your comment'
        context['action'] ='edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('all_comment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Comment Forms'
        context['table_tittle'] = 'Delete comment Form'
        context['table_subtittle'] = 'Delete here your comment'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

