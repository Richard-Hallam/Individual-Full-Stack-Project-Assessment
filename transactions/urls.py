from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('transactions', views.transactions_list, name='transactions_list'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)