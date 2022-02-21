""" proverb app views """
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proverb
from .forms import ProverbForm


def home(request):
    """
    home view
    generates a random proverb and meaning
    """
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


def list_proverbs(request):
    """ generates a list with all proverbs """
    all_proverbs = Proverb.objects.all()
    print(f'all proverbs: {all_proverbs}')                  # testing
    context = {'all_proverbs': all_proverbs}
    return render(request, 'proverbs.html', context)


def add_proverb(request):
    """ add proverb view """
    # add POST functionality
    if request.method == 'POST':
        form = ProverbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    # GET functionality
    form = ProverbForm()
    context = {'form': form}
    return render(request, 'add-proverb.html', context)


def edit_proverb(request, pk):
    """ edit proverb view """
    print(f'edit_id={pk}')                                  # testing
    proverb = get_object_or_404(Proverb, id=pk)
    # add POST functionality
    if request.method == 'POST':
        form = ProverbForm(request.POST, instance=proverb)
        if form.is_valid():
            form.save()
            return redirect('home')

    # GET functionality
    form = ProverbForm(instance=proverb)
    context = {'form': form}
    return render(request, 'edit-proverb.html', context)
