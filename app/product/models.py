from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=15)
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/')
