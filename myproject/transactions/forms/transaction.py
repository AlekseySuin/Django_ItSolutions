from django import forms
from ..models.transaction import Transaction
from ..models.subcategory import SubCategory


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"