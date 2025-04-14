from ...models.transaction_type import TransactionType
from ...forms.transaction_type import TransactionTypeForm
from .base import *


class TransactionTypeBaseView:
    model = TransactionType
    form_class = TransactionTypeForm


class TransactionTypeListView(TransactionTypeBaseView, ReferenceListView):
    context_object_name = 'transaction_types'


class TransactionTypeCreateView(TransactionTypeBaseView, ReferenceCreateView):
    ...


class TransactionTypeUpdateView(TransactionTypeBaseView, ReferenceUpdateView):
    ...


class TransactionTypeDeleteView(TransactionTypeBaseView, ReferenceDeleteView):
    ...