from ...models.status import Status
from ...forms.status import StatusForm
from .base import *
from django.urls import reverse_lazy


class StatusBaseView:
    model = Status
    form_class = StatusForm

# Можно добавить дополнительную логику для каждого случая при необходимости
class StatusListView(StatusBaseView, ReferenceListView):
    context_object_name = 'statuses'


class StatusCreateView(StatusBaseView, ReferenceCreateView):
    ...


class StatusUpdateView(StatusBaseView, ReferenceUpdateView):
    ...


class StatusDeleteView(StatusBaseView, ReferenceDeleteView):
    ...