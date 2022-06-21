from django import forms
from .models import Model

class model_form(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ['prediction']