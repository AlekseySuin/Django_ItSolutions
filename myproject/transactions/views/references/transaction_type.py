from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ...models.transaction_type import TransactionType
from ...forms.transaction_type import TransactionTypeForm
from django.urls import reverse_lazy


class TransactionTypeBaseView:
    model = TransactionType
    form_class = TransactionTypeForm
    success_url = reverse_lazy('references:transactiontype_list')


class TransactionTypeListView(TransactionTypeBaseView, ListView):
    template_name = 'transactions/references/list.html'
    context_object_name = 'transaction_types'


class TransactionTypeCreateView(TransactionTypeBaseView, CreateView):
    template_name = 'transactions/references/form.html'


class TransactionTypeUpdateView(TransactionTypeBaseView, UpdateView):
    template_name = 'transactions/references/form.html'


class TransactionTypeDeleteView(TransactionTypeBaseView, DeleteView):
    template_name = 'transactions/references/delete_confirm.html'