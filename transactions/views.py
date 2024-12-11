from django.template import loader
from .forms import TransactionForm
from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib import messages
from django.http import HttpResponse


def transactions_list(request):
    if request.method == 'POST':
        form = TransactionForm(data=request.POST)
        form.save()
        messages.add_message(
            request, messages.SUCCESS,
            'transaction submitted succsessfully'
        )
        #return render(request, 'transactions/transaction_list.html')
        return(redirect('transactions_list'))
    else:
        form = TransactionForm()
        transactions = Transaction.objects.all()
        context = {'form': form}
        #return render(request, 'transactions/transaction_list.html', context)
        return render(request, 'transactions/transaction_list.html', {'transactions': transactions, 'form': form})


def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            transactions = Transaction.objects.all()
            return redirect('transactions/transactions_list', {'transactions' : transactions })
    else:
        form = TransactionForm(instance=transaction)
        transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions_edit.html', {'transactions': transactions, 'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions_list')
    return render(request, 'transactions/delete_transaction.html', {'transactions': transaction})