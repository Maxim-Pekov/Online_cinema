from django import forms
from .models import Reviews, Rating, RatingStar


class ReviewsForms(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'name', 'email']


class RatingForm(forms.ModelForm):
    '''Форма добавления рейтинга'''

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta():
        model = Rating
        fields = ('star',)
