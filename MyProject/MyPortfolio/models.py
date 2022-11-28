from asyncio.windows_events import NULL
import email
from email import message
from pyexpat import model
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    subject = models.TextField(max_length=20, null=True)
    message = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name
    