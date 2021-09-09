from django.db import models

# Create your models here.
class Product(models.Model):
    date = models.DateField()
    provider = models.CharField(max_length=30)
    name_of_product = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    stock = models.IntegerField()
