from django.urls import path, include

urlpatterns = [
    path('statuses/', include('transactions.urls.statuses')),
    path('categories/', include('transactions.urls.categories')),
]