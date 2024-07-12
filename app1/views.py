from django.shortcuts import render
import math

def calculate(request):
    n1 = 5
    square = n1 ** 2
    factorial = math.factorial(n1)
    context = {
        'square': square,
        'factorial': factorial
    }
    return render(request, 'app1/result.html', context)
