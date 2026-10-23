from django import forms
from .models import ContactMesssage

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMesssage
        fields='__all__'

