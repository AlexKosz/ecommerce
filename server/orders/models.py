from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product
import uuid
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # $0.01 - $10,000.00
    order_total_in_cents = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10_000_00)])

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    delivered_on = models.DateTimeField(null=True, blank=True)

    shipping_carrier = models.CharField(max_length=100, null=True, blank=True)
    tracking_number = models.CharField(max_length=100, null=True, blank=True)

    shipping_st = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=16)
    shipping_zip = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99999)])

    recipient_first = models.CharField(max_length=30)
    recipient_last = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, blank=True)
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
