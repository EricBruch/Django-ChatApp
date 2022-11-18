from django.db import models
from django.db.models.fields import DateField
from datetime import date
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = DateField(default=now)
    #chat = mit chat vernüofen
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')