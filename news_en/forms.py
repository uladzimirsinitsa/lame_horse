from django import forms
from .models import NewsEn
from django.db import models


class NewsFormEn(forms.ModelForm):
    body = models.TextField()

    class Meta:
        model = NewsEn
        fields = ['title', 'body', 'description']
