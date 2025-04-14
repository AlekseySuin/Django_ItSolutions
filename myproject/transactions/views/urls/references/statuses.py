from django.urls import path
from ...references.status import (
    StatusListView,
    StatusCreateView,
    StatusDeleteView,
    StatusUpdateView
)

app_name = 'status'

urlpatterns = [
    path('', StatusListView.as_view(), name='list'),
    path('create/', StatusCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', StatusUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete'),
]