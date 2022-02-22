""" proverb app views """
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proverb
from .forms import ProverbForm


def home(request):
    """
    home view
    generates a random proverb and meaning
    """
    max_records = Proverb.objects.all()
    print(f'max_records: {max_records}')                    # testing
    records_ids = [max_record.id for max_record in max_records]
    print(f'records_ids: {records_ids}')                    # testing
    random_id = random.choice(records_ids)
    print(f'random_id: {random_id}')                        # testing
    random_proverb_obj = Proverb.objects.get(id=random_id)
    print(f'random_proverb_obj = {random_proverb_obj}')     # testing

    context = {
        'id': random_proverb_obj.id,
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


@login_required
def add_proverb(request):
    """ add proverb view """
    # add POST functionality
    if request.method == 'POST':
        form = ProverbForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')

    # GET functionality
    form = ProverbForm()
    context = {'form': form}
    return render(request, 'add-proverb.html', context)


@login_required
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


@login_required
def delete_proverb(request, proverb_id):
    """ delete proverb view """
    proverb = get_object_or_404(Proverb, id=proverb_id)
    if request.user == proverb.author:
        proverb.delete()
    return redirect('home')
