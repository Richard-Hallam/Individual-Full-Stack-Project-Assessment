from django.template import loader
from .forms import TransactionForm
from django.shortcuts import render
from .models import Transaction
from django.contrib import messages

def transactions_list(request):
    if request.method == 'POST':
        form = TransactionForm(data=request.POST)
        form.save()
        messages.add_message(
            request, messages.SUCCESS,
            'transaction submitted succsessfully'
        )
    else:
        form = TransactionForm()
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions, 'form': form})