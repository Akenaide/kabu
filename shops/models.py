from typing import override
from django.db import models

from django_countries.fields import CountryField

# Create your models here.


class Shop(models.Model):
    name = models.CharField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    country = CountryField()

    @override
    def __str__(self):
        return f"{self.pk} - {self.name}"
