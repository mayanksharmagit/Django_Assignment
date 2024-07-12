from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def generate_account_number():
    last_customer = Customer.objects.all().order_by('id').last()
    if not last_customer:
        return '8000'
    last_account_number = int(last_customer.account_number)
    new_account_number = last_account_number + 1
    return str(new_account_number)

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.account_number = generate_account_number()
            customer.save()
            return render(request, 'accounts/success.html', {'account_number': customer.account_number})
    else:
        form = CustomerForm()
    return render(request, 'accounts/customer_form.html', {'form': form})
