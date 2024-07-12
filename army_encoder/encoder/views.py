from django.shortcuts import render
from .utils import encode_message

def encode_message_view(request):
    if request.method == "POST":
        message = request.POST.get('message', '')
        encoded_message = encode_message(message)
        return render(request, 'encoder/result.html', {'encoded_message': encoded_message})

    return render(request, 'encoder/encode.html')
