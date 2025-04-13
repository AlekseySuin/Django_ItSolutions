from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages


class ReferenceBookView(View):
    """Универсальный CRUD View для всех справочников"""
    model = None  # Должно быть задано в наследнике
    form_class = None  # Должно быть задано в наследнике
    base_template = 'transactions/base.html'
    list_url_name = None  # Например: 'references:status_list'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {
            'model_meta': self.model._meta,
            'object': getattr(self, 'object', None),
            'object_list': self.get_queryset(),
            'view': self,
            'title': self.model._meta.verbose_name_plural,
        }
        context.update(kwargs)
        return context

    def get(self, request, pk=None, action=None):
        context = {}

        if action == 'create':
            context['form'] = self.form_class()
        elif action == 'edit' and pk:
            item = get_object_or_404(self.model, pk=pk)
            context['form'] = self.form_class(instance=item)
        elif action == 'delete' and pk:
            item = get_object_or_404(self.model, pk=pk)
            item.delete()
            messages.success(request, f'{self.model._meta.verbose_name} удален')
            return redirect(self.get_success_url())

        return render(
            request,
            self.get_template(action),
            self.get_context_data(**context)
        )

    def post(self, request, pk=None, action=None):
        form = self.form_class(
            request.POST,
            instance=self.model(pk=pk) if pk else None
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect(self.get_success_url())

        return render(
            request,
            self.get_template(action),
            self.get_context_data(form=form)
        )

    def get_success_url(self):
        return reverse(self.list_url_name)

    def get_template(self, action):
        return f'transactions/references/{action}.html' if action else self.base_template