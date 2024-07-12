from django.urls import path
from . import views

urlpatterns = [
    path('', views.perm_input, name='perm_input'),
    path('calculate/', views.display_permutations, name='display_permutations'),
]
