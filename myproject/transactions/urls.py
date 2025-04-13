from django.urls import path, include

urlpatterns = [
    path('', include('transactions.urls.operations')),  # Основные операции
    path('references/', include('transactions.urls.references')),  # Справочники
]