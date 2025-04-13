from django.urls import path
from ...views.references.subcategory import (
    SubCategoryListView,
    SubCategoryCreateView,
    SubCategoryDeleteView,
    SubCategoryUpdateView
)

app_name = 'sub_category'

urlpatterns = [
    path('', SubCategoryListView.as_view(), name='list'),
    path('create/', SubCategoryCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', SubCategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SubCategoryDeleteView.as_view(), name='delete'),
]