from django.db import models
from .category import Category


class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название подкатегории"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['name']
        unique_together = [['name', 'category']]

    def __str__(self):
        return f"{self.category} → {self.name}"