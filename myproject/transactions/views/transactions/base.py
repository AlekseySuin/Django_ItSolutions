from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ...models.transaction import Transaction
from ...forms.transaction import TransactionForm


class TransactionMixin:
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('transactions:list')


class TransactionListView(TransactionMixin, ListView):
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'
    paginate_by = 20


class TransactionCreateView(TransactionMixin, CreateView):
    template_name = 'transactions/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(TransactionMixin, UpdateView):
    template_name = 'transactions/form.html'


class TransactionDeleteView(TransactionMixin, DeleteView):
    template_name = 'transactions/confirm_delete.html'