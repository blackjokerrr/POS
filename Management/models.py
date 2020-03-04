from django.db import models


class Order(models.Model):
    date_time = models.DateField(null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    type_of = models.ForeignKey(Type, on_delete=models.PROTECT)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    orders = models.ManyToManyField(Order, through='Sale.Order_Product')
    def __str__(self):
        return self.name
