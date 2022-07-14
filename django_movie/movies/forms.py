from django import forms
from .models import Reviews

class ReviewsForms(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'name', 'email']

