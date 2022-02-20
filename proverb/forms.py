""" forms file """
from django import forms
from .models import Proverb


# create a form to add a proverb
class ProverbForm(forms.ModelForm):
    """ create form here """
    class Meta:
        """ info about form """
        model = Proverb
        fields = ['content', 'meaning', 'author']
