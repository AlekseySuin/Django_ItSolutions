from django.urls import path
from ..transactions.base import (
    TransactionUpdateView,
    TransactionDeleteView,
    TransactionCreateView,
    TransactionListView
)

app_name = 'transactions'

urlpatterns = [
    path('',
         TransactionListView.as_view(),
         name='list'),

    path('create/',
         TransactionCreateView.as_view(),
         name='create'),

    path('<int:pk>/update/',
         TransactionUpdateView.as_view(),
         name='update'),

    path('<int:pk>/delete/',
         TransactionDeleteView.as_view(),
         name='delete'),
]