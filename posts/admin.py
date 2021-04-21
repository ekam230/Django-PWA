from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.

from .models import feed

admin.site.register(feed)