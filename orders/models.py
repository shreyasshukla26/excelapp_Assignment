from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.order_id} - {self.product_name}'
