from django.db import models
from django.contrib.auth.models import User
import uuid
from products.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    product = models.ManyToManyField(
        Product, blank=True)
