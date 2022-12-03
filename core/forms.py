from django import forms
from django.forms import ModelForm

from core.models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Taks
        fields ='__all__'

