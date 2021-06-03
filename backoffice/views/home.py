from django.shortcuts import render
from django.contrib.auth.models import User
from backoffice.models import User
from django.views.generic import  TemplateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators  import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required



# Create your views here.


""" layouts"""


""" root own backoffice"""
"""
class BackoficeListView(ListView):
    template_name ='layouts/backoffice.html'
"""
@login_required()
def management(request):
    return render(request,'layouts/backoffice.html')
    


class index(LoginRequiredMixin, TemplateView):
    template_name = 'layouts/backoffice.html'

    def get_context_data(self, *args, **kwargs):
        chats = Chat.objects.all()
        tasks = Task.objects.all()
        comments = Comment.objects.all()
        items = Item.objects.all()
        posts = Post.objects.all()
        returneds = Returned.objects.all()
        solds = Sold.objects.all()
        return {'chats': chats, 'tasks': tasks, 'comments':comments, 'items':items, 'posts':post, 'returneds':returned, 'solds':sold}

"""
def access(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
"""

def forms(request):
    return render(request, 'forms.html')


def tables(request):
    return render(request, 'tables.html')


def charts(request):
    return render(request, 'charts.html')


def side_navbar(request):
    return render(request, 'side_navbar.html')


def brand(request):
    return render(request, 'brand.html')


def user_nav(request):
    return render(request, 'user_nav.html')


def usuario(request):
    return render(request, 'usuario.html')


def logo(request):
    return render(request, 'logo.html')


def menu(request):
    return render(request, 'menu.html')


def header(request):
    return render(request, 'header.html')


def top_menu(request):
    return render(request, 'top_menu.html')


def notifications(request):
    return render(request, 'notifications.html')


def mails(request):
    return render(request, 'mails.html')


def languajes(request):
    return render(request, 'languajes.html')


def content_header(request):
    return render(request, 'content_header.html')


def todo_list(request):
    return render(request, 'todo_list.html')


def counter(request):
    return render(request, 'counter.html')


def dashboard_chart_1(request):
    return render(request, 'dashboard_chart_1.html')


def dashboard_chart_2(request):
    return render(request, 'dashboard_chart_2.html')


def statistics(request):
    return render(request, 'statistics.html')


def updates(request):
    return render(request, 'updates.html')


"""pages"""


"""related company pages"""


def company_details(request):
    return render(request, 'company_details.html')



def general_charts(request):
    return render(request, 'general_charts.html')


def social(request):
    return render(request, 'social.html')


def statistics_page(request):
    return render(request, 'statistics_page.html')


def chat(request):
    return render(request, 'chat.html')