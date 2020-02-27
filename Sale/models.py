from django.db import models

from Management.models import Order, Product

class Order_Product(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()