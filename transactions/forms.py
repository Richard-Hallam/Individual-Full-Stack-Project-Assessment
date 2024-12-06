from .models import Transaction
from django import forms

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('transaction_name', 'transaction_date', 'transaction_amount',
            'expense', 'account', 'category',)