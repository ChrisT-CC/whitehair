""" proverb app views """
from django.shortcuts import render


def home(request):
    """ Home view """
    return render(request, 'home.html')
