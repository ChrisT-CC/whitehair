""" forms file """
from django.forms import ModelForm, Textarea
from .models import Proverb


# create a form to add a proverb
class ProverbForm(ModelForm):
    """ create form here """
    class Meta:
        """ info about form """
        model = Proverb
        fields = '__all__'
        widgets = {
            'meaning': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        labels = {
            'content': ('Add your proverb here'),
            'meaning': ('Explain it here'),
            'author': ('Select your username as author'),
        }
