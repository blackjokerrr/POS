from django.db import models

from Management.models import Order, Product

class Order_Product(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()
    def __str__(self):
        return self.product_id.name + ' ' + str(self.product_id.price) + ' ' + str(self.amount) + ' EA'
    

class Order_Product_Storage(models.Model):
    storage_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    storage_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    storage_amount_all = models.IntegerField()
    storage_price_all = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return str(self.storage_order.date_time) + ' ' + self.storage_product.name + ' ' + str(self.storage_price_all) + ' Baht ' + str(self.storage_amount_all) + ' item'