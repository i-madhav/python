from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2048)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 