from django.contrib import admin
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Register your models here.

admin.site.register(Snippet)
