from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ...models.subcategory import SubCategory
from ...forms.subcategory import SubCategoryForm
from django.urls import reverse_lazy


class SubCategoryBaseView:
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('references:subcategory_list')


class SubCategoryListView(SubCategoryBaseView, ListView):
    template_name = 'transactions/references/list.html'
    context_object_name = 'subcategories'


class SubCategoryCreateView(SubCategoryBaseView, CreateView):
    template_name = 'transactions/references/form.html'


class SubCategoryUpdateView(SubCategoryBaseView, UpdateView):
    template_name = 'transactions/references/form.html'


class SubCategoryDeleteView(SubCategoryBaseView, DeleteView):
    template_name = 'transactions/references/delete_confirm.html'
