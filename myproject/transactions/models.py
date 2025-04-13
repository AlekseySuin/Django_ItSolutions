from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name='Статус транзакции'
        verbose_name_plural='Статусы транзакций'
        ordering=['name']

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TransactionSubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.category} - {self.name}"


class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    record_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.record_date} - {self.amount} - {self.status}"