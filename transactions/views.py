from django.template import loader
from .forms import TransactionForm
from django.shortcuts import render
from .models import Transaction

def transactions_list(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions_list')
    else:
        form = TransactionForm()
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions, 'form': form})