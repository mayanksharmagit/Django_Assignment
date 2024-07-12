from django.shortcuts import render
import math

def factorial_input(request):
    return render(request, 'app3/factorial_input.html')

def display_factorials(request):
    if request.method == 'POST':
        try:
            start = int(request.POST.get('start'))
            end = int(request.POST.get('end'))
            if 3 <= start <= 8 and 3 <= end <= 8 and start <= end:
                factorials = {i: math.factorial(i) for i in range(start, end + 1)}
                return render(request, 'app3/factorial_result.html', {'factorials': factorials})
            else:
                return render(request, 'app3/factorial_error.html')
        except ValueError:
            return render(request, 'app3/factorial_error.html')
    else:
        return render(request, 'app3/factorial_input.html')
