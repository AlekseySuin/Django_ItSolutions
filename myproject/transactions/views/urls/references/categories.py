from django.urls import path
from ...references.category import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),
]