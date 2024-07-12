from django.shortcuts import render
import math

def factorial_input(request):
    return render(request, 'app2/factorial_input.html')

def calculate_factorial(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        if 1 <= number <= 10:
            factorial = math.factorial(number)
            return render(request, 'app2/factorial_result.html', {'number': number, 'factorial': factorial})
        else:
            return render(request, 'app2/factorial_error.html')
