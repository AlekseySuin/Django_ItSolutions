from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ...models.transaction import Transaction
from ...forms.transaction import TransactionForm
from ..references.subcategory import SubCategory
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)


class TransactionMixin:
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST', 'GET'):
            kwargs.update({
                'data': self.request.POST if self.request.method == 'POST' else None
            })
        return kwargs


class TransactionListView(TransactionMixin, ListView):
    template_name = 'transactions/transactions_list.html'
    context_object_name = 'transactions'
    paginate_by = 20


class TransactionCreateView(TransactionMixin, CreateView):
    template_name = 'transactions/transaction_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = SubCategory.objects.all()
        return context


class TransactionUpdateView(TransactionMixin, UpdateView):
    template_name = 'transactions/transaction_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = SubCategory.objects.all()

        # Получаем ID подкатегории из POST данных или из дополнительного поля
        if self.request.method == 'POST':
            context['subcategory_id'] = self.request.POST.get('subcategory')

        return context


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/delete_confirm.html'
    success_url = reverse_lazy('transactions:list')

    def post(self, request, *args, **kwargs):
        logger.info("=== Начало обработки DELETE запроса ===")

        # Проверяем, что кнопка удаления была нажата
        if 'confirm_delete' not in request.POST:
            logger.warning("Кнопка удаления не была нажата!")
            return HttpResponseRedirect(self.get_success_url())

        self.object = self.get_object()
        logger.info(f"Объект для удаления: {self.object}")

        try:
            # Явное удаление объекта
            delete_result = self.object.delete()
            logger.info(f"Результат удаления: {delete_result}")

            if delete_result[0] == 0:
                logger.error("Объект не был удален!")
            else:
                logger.info("Объект успешно удален")

        except Exception as e:
            logger.error(f"Ошибка при удалении: {str(e)}")
            raise

        logger.info("=== Завершение обработки DELETE запроса ===")
        return HttpResponseRedirect(self.get_success_url())