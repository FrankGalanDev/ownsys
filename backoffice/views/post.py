from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import  ListView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from backoffice.forms import PostForm
from backoffice.models import Post
from django.core.paginator import Paginator



# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/all_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Post List'
        context['table_subtittle'] = 'All posts'
        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/new_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Post Forms'
        context['table_tittle'] = 'New post'
        context['table_subtittle'] = 'Add here your new post'
        context['action'] ='add'
        return context
    
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('all_post')


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update_post.html'
    success_url = reverse_lazy('all_post')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Post Forms'
        context['table_tittle'] = 'Edit post'
        context['table_subtittle'] = 'Modify here your post'
        context['action'] ='edit'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('all_post')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Post Forms'
        context['table_tittle'] = 'Delete post Form'
        context['table_subtittle'] = 'Delete here your post'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


