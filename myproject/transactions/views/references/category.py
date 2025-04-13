from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ...models.category import Category
from ...forms.category import CategoryForm
from django.urls import reverse_lazy


class CategoryBaseView:
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('references:category_list')


class CategoryListView(CategoryBaseView, ListView):
    template_name = 'transactions/references/list.html'
    context_object_name = 'categories'


class CategoryCreateView(CategoryBaseView, CreateView):
    template_name = 'transactions/references/form.html'


class CategoryUpdateView(CategoryBaseView, UpdateView):
    template_name = 'transactions/references/form.html'


class CategoryDeleteView(CategoryBaseView, DeleteView):
    template_name = 'transactions/references/delete_confirm.html'