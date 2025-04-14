from django.urls import path
from ...references.transaction_type import (
    TransactionTypeListView,
    TransactionTypeCreateView,
    TransactionTypeDeleteView,
    TransactionTypeUpdateView
)

app_name = 'transaction_type'

urlpatterns = [
    path('', TransactionTypeListView.as_view(), name='list'),
    path('create/', TransactionTypeCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', TransactionTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='delete'),
]