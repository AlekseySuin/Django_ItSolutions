from django import forms
from ..models.transaction_type import TransactionType


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = "__all__"