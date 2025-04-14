from django.urls import path, include

app_name = 'references'

urlpatterns = [
    path('statuses/', include('transactions.views.urls.references.statuses')),
    path('categories/', include('transactions.views.urls.references.categories')),
    path('types/', include('transactions.views.urls.references.transaction_types')),
    path('subcategories/', include('transactions.views.urls.references.subcategories')),
]