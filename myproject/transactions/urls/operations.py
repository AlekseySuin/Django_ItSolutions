from django.urls import path
from ..views.transactions.base import TransactionListView, TransactionCreateView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
]