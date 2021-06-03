
from django.contrib.auth.models import User
from backoffice.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.templatetags.static import static
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from backoffice.models import Chat
from django.core import serializers
from backoffice.serializer.chat import serialize as serialize_chat
from django.core.serializers import serialize



# Create your views here.

class ChatView(LoginRequiredMixin, View):
    model = Chat
    template_name = 'chats/all_chats.html',


    def get(self, request):
        return render(request, 'chats/all_chats.html')

    def post(self, request):
        chat = Chat(text=request.POST['message'], owner=request.user)
        chat.save()
        return redirect(reverse('all_chat'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ChatMessagesView(LoginRequiredMixin, View):

    def get(self, request):
        User = get_user_model()

        messages = Chat.objects.all().order_by('created_at')[10:]
       
        
        results = []
        for message in messages:

        #    result = [message.text, naturaltime(message.created_at)]
            result = [serialize_chat(chat=message, embed=['user'])]
            results.append(result)
        return JsonResponse(results, safe=False)



