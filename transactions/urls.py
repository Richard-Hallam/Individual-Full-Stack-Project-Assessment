from django.urls import path
from . import views

urlpatterns = [
    path('transactions', views.transactions_list, name='transactions_list'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]