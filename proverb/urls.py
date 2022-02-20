""" Proverb URL Configuration """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-proverb/', views.add_proverb, name='add_proverb'),
    # path('edit-proverb/<int:proverb_id>', views.edit_proverb, name='edit_proverb'),
]
