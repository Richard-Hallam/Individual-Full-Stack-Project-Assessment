from django.contrib import admin

from .models import Transaction
from .models import Account
from .models import Category
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Category)