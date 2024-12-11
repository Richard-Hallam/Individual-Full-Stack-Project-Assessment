from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions_list, name='transaction_list'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
]