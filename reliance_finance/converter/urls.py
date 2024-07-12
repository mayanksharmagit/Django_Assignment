from django.urls import path
from .views import convert_figure

urlpatterns = [
    path('', convert_figure, name='convert_figure'),
]
