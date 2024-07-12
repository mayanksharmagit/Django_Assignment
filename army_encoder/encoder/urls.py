from django.urls import path
from .views import encode_message_view

urlpatterns = [
    path('', encode_message_view, name='encode_message'),
]
