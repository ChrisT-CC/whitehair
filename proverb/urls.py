""" Proverb URL Configuration """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('proverbs/', views.list_proverbs, name='list_proverbs'),
    path('add-proverb/', views.add_proverb, name='add_proverb'),
    path('edit-proverb/<int:pk>', views.edit_proverb, name='edit_proverb'),
    path(
        'delete-proverb/<int:proverb_id>',
        views.delete_proverb,
        name='delete_proverb'
        ),
]
