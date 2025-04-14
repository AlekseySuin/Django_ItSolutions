from ...models.subcategory import SubCategory
from ...forms.subcategory import SubCategoryForm
from .base import *


class SubCategoryBaseView:
    model = SubCategory
    form_class = SubCategoryForm


class SubCategoryListView(SubCategoryBaseView, ReferenceListView):
    context_object_name = 'subcategories'


class SubCategoryCreateView(SubCategoryBaseView, ReferenceCreateView):
    ...


class SubCategoryUpdateView(SubCategoryBaseView, ReferenceUpdateView):
    ...


class SubCategoryDeleteView(SubCategoryBaseView, ReferenceDeleteView):
    ...
