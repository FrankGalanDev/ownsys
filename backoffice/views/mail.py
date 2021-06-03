from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from backoffice.models import User
from django.template.loader import render_to_string




class MailView(LoginRequiredMixin, TemplateView):
    template_name = 'email_prototype.html'
    model = User


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
