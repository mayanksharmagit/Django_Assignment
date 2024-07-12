from django.urls import path
from . import views

urlpatterns = [
    path('', views.factorial_input, name='factorial_input'),
    path('calculate/', views.calculate_factorial, name='calculate_factorial'),
]
