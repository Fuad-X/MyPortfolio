from distutils.log import info
import imp
from django.contrib import admin
from .models import Info

# Register your models here.
admin.site.register(Info)