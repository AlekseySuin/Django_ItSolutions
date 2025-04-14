from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import logging


logger = logging.getLogger(__name__)

class ReferenceBaseView:
    template_name = None  # Должен быть переопределен
    success_url = None  # Должен быть переопределен

    def get_success_url(self):
        return self.success_url or reverse_lazy(f'references:{self.model._meta.model_name}:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.model._meta.model_name
        context['create_url'] = f'references:{model_name}:create'
        context['update_url'] = f'references:{model_name}:update'
        context['delete_url'] = f'references:{model_name}:delete'
        context['list'] = f'references:{model_name}:list'
        context['model_meta'] = self.model._meta
        return context


class ReferenceListView(ReferenceBaseView, ListView):
    template_name = 'transactions/references/list.html'
    context_object_name = 'object_list'


class ReferenceCreateView(ReferenceBaseView, CreateView):
    template_name = 'transactions/references/form.html'


class ReferenceUpdateView(ReferenceBaseView, UpdateView):
    template_name = 'transactions/references/form.html'


class ReferenceDeleteView(ReferenceBaseView, DeleteView):
    template_name = 'transactions/references/delete_confirm.html'

    def post(self, request, *args, **kwargs):
        logger.info(f"Начало обработки удаления для {self.model.__name__}")

        # Проверяем, что кнопка удаления была нажата
        if 'confirm_delete' not in request.POST:
            logger.warning("Кнопка удаления не была нажата!")
            return HttpResponseRedirect(self.get_success_url())

        self.object = self.get_object()
        logger.info(f"Объект для удаления: {self.object} (ID: {self.object.pk})")

        try:
            # Явное удаление объекта
            delete_result = self.object.delete()
            logger.info(f"Результат удаления: {delete_result}")

            if delete_result[0] == 0:
                logger.error("Объект не был удален!")
            else:
                logger.info(f"Успешно удалено {delete_result[0]} записей")

        except Exception as e:
            logger.error(f"Ошибка при удалении: {str(e)}")
            raise

        return HttpResponseRedirect(self.get_success_url())