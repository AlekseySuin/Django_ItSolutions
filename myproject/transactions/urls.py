from django.urls import path, include

urlpatterns = [
    path('', include('transactions.views.urls.transactions')),
    path('references/', include('transactions.views.urls.references')),
]