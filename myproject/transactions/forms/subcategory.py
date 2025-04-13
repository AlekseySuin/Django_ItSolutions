from django import forms
from ..models.subcategory import SubCategory


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"