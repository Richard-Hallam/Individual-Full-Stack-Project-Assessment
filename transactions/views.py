from django.template import loader
from .forms import TransactionForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from django.contrib import messages
from django.http import HttpResponse


def get_total_transaction_value(transactions):
    """sums all transactions and returns the total"""
    total = 0
    for transaction in transactions:
        total = total + transaction.transaction_amount
    return total


def transactions_list(request):
    if request.method == 'POST':
        form = TransactionForm(data=request.POST)
        form.save()
        messages.add_message(
            request, messages.SUCCESS,
            'transaction submitted succsessfully'
        )
        return(redirect('transactions_list'))
    else:
        form = TransactionForm()
        transactions = Transaction.objects.all()
        total_transaction_value = get_total_transaction_value(transactions)
        context = {
            'transactions': transactions,
            'form': form,
            'total_transaction_value': total_transaction_value,
                }
        
        return render(request, 'transactions/transaction_list.html', context)


def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            transactions = Transaction.objects.all()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/transaction_edit.html', { 'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Transaction deleted successfully'
        )
        return redirect('transactions_list')
    return render(request, 'transactions/transaction_delete.html', {'transaction': transaction})

