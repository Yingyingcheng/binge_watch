# binge_watch_app/admin.py

from django.contrib import admin
from .models import Content, Review

# Register your models here.
admin.site.register(Content)
admin.site.register(Review)