from typing import override
from django.db import models

# Create your models here.


class Player(models.Model):
    identifier = models.CharField(unique=True)
    verbose_name = models.CharField(blank=True)

    @override
    def __str__(self):
        return f"{self.pk} - {self.identifier}"
