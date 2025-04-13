from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ...models.status import Status
from ...forms.status import StatusForm
from django.urls import reverse_lazy


class StatusBaseView:
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('references:status_list')


class StatusListView(StatusBaseView, ListView):
    template_name = 'transactions/references/list.html'
    context_object_name = 'statuses'


class StatusCreateView(StatusBaseView, CreateView):
    template_name = 'transactions/references/form.html'


class StatusUpdateView(StatusBaseView, UpdateView):
    template_name = 'transactions/references/form.html'


class StatusDeleteView(StatusBaseView, DeleteView):
    template_name = 'transactions/references/delete_confirm.html'