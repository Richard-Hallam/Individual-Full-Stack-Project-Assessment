from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_name = models.CharField(max_length=255)
    transaction_date = models.DateField()
    transaction_amount = models.FloatField()
    expense = models.BooleanField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_name
    
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=255)
    account_value = models.FloatField(default=0.0)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)