from django.db import models
from .status import Status
from .category import Category
from .transaction_type import TransactionType


class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    record_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.record_date} - {self.amount} - {self.status}"