from django.db import models

from Management.models import Order, Product

class Order_Product(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return self.product_id.name + ' ' + str(self.product_id.price) + ' ' + str(self.amount) + ' EA'
    
class Save_Product(models.Model):
    order_all = models.ForeignKey(Order_Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.order_all.order_id.date_time) + ' ' + str(self.order_all.product_id.price)