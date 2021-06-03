from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='created_by',
        null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='updated_by',
        null=True, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
