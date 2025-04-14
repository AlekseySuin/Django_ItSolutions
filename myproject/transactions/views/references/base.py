from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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