from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    types = models.CharField(max_length=30)
    original_price = models.CharField(max_length=30)
    discount_price = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Review(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=30)

class Rating(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    star = models.CharField(max_length=30)

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=30)

class Tags(models.Model):
    name = models.CharField(max_length=30)
     
class Product_Tags(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)  

class Address(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)



    
