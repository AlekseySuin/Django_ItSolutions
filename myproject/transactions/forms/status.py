from django import forms
from ..models.status import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"