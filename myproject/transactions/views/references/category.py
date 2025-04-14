from ...models.category import Category
from ...forms.category import CategoryForm
from .base import *


class CategoryBaseView:
    model = Category
    form_class = CategoryForm


class CategoryListView(CategoryBaseView, ReferenceListView):
    context_object_name = 'categories'


class CategoryCreateView(CategoryBaseView, ReferenceCreateView):
    ...


class CategoryUpdateView(CategoryBaseView, ReferenceUpdateView):
    ...


class CategoryDeleteView(CategoryBaseView, ReferenceDeleteView):
    ...