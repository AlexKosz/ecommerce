from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    qty_avail = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    #$0.01 - $1000.00
    price_in_cents = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100_000)])
    # Rating from 0.00 - 5.00
    average_star_rating = models.DecimalField(max_digits=3, decimal_places= 2, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

#many-many orders
#many-many related products
#many-many? with join table for users items in carts

    # Not used in this project - warehouse_location = models.CharField(max_length=200, null=True, blank=True) 

class Review(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places= 1)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)

