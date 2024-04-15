from django.db import models


class Currency(models.Model):
    sale = models.DecimalField(max_digits=5,decimal_places=2)
    buy = models.DecimalField(max_digits=5,decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3)
    source = models.CharField(max_length=64)
