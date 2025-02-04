"""
URL configuration for expensetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_page, login, account_signup
from transactions.views import transactions_list, edit_transaction
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('transactions/', transactions_list, name='transactions'),
    path('transactions/', include('transactions.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/<int:transaction_id>/', edit_transaction, name='edit_transaction'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
