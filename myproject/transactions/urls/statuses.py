from django.urls import path
from myproject.transactions.views.references.status import (
    StatusListView,
    StatusCreateView,
    StatusDeleteView,
    StatusUpdateView
)

app_name = 'status'

urlpatterns = [
    path('', StatusListView.as_view(), name='list'),
    path('create/', StatusCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', StatusDeleteView.as_view(), name='update'),
    path('<int:pk>/delete/', StatusUpdateView.as_view(), name='delete'),
]