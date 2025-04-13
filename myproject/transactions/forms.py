from django import forms
from .models import *


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = "__all__"


class TransactionCategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionCategory
        fields = "__all__"


class TransactionSubCategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionSubCategory
        fields = "__all__"


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"