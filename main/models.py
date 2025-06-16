from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    discount = models.IntegerField(null=True, blank=True)#
    is_new = models.BooleanField(default=True)#
    image = models.ImageField(upload_to='media/')#
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#
    name = models.CharField(max_length=100)#
    price = models.FloatField()#
    new_price = models.FloatField(null=True, blank=True)
    text = models.TextField()#
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.first_name


class News(models.Model):
    name = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='media/')
    date_created = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return self.name
    

from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
