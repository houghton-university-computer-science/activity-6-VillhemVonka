from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    order_date = models.DateField()

class Product(models.Model):
    product_id = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])

class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    mailing_address = models.TextField()
    email = models.TextField()
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    pass