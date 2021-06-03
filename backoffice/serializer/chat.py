from django.contrib.auth.models import User
from backoffice.models import User
from rest_framework import serializers
from backoffice.serializer.user import serialize as serialize_user
from django.contrib.humanize.templatetags.humanize import naturaltime


def serialize(chat, embed=None):
    return {
        'id': chat.id,
        'message': chat.text,
        'created_at': naturaltime(chat.created_at),
        'owner': serialize_user(user=chat.owner) if 'user' in embed else chat.owner.id
    }