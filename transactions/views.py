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

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/edit_transaction.html', {'form': form})
