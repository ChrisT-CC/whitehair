""" proverb app views """
import random
from django.shortcuts import render
from .models import Proverb


def home(request):
    """ Home view """
    max_records = Proverb.objects.all().count()
    random_id = random.randint(1, max_records)
    random_proverb_obj = Proverb.objects.get(id=random_id)
    print(f'id = {random_id}')                              # testing
    print(f'random_proverb_obj = {random_proverb_obj}')     # testing
    context = {
        'content': random_proverb_obj.content,
        'meaning': random_proverb_obj.meaning,
    }
    print(f'context is: {context}')                         # testing
    return render(request, 'home.html', context)


def add_proverb(request):
    """ add proverb view """
    context = {}
    return render(request, 'add-proverb.html', context)
