from dataclasses import fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from wsgiref.handlers import format_date_time
from xml.dom import VALIDATION_ERR
from django import forms
from django.forms import ValidationError
from .models import Tweet


MAX_TWEET_LENGTH = 250

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):    
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("THIS is too long try to do it short than 250")
        return content

        