from django.db import models


class TransactionType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Тип операции"
    )

    class Meta:
        verbose_name = "Тип транзакции"
        verbose_name_plural = "Типы транзакций"
        ordering = ['name']

    def __str__(self):
        return self.name