from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class DisplayModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    class Meta:
        verbose_name = "budíček"
        verbose_name_plural = "Zde se nastavuje přístupnost na stránce"

    def __str__(self):
        return self.title

