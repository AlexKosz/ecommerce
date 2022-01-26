from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    qty_avail = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    
    #$0.01 - $1000.00
    price_in_cents = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100_000)])

    # Rating from 0.00 - 5.00
    average_star_rating = models.DecimalField(max_digits=3, decimal_places= 2, null=True, blank=True)




#images

#many-many orders
#many-many tags
#many-many reviews
#many-many related products

#many-many? with join table for users items in carts




#Not used in this app
# warehouse_location = models.CharField(max_length=200, null=True, blank=True)