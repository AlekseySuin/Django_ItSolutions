from django.urls import path, include

app_name = 'references'

urlpatterns = [
    path('statuses/', include('transactions.urls.references.statuses')),
    path('categories/', include('transactions.urls.references.categories')),
    path('types/', include('transactions.urls.references.transaction_types')),
    path('subcategories/', include('transactions.urls.references.subcategories')),
]