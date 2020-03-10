from django.db import models


class Order(models.Model):
    date_time = models.DateField(auto_now=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_all = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return str(self.date_time)

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
    storage = models.SmallIntegerField()
    orders = models.ManyToManyField(Order, through='Sale.Order_Product')
    def __str__(self):
        return self.name



