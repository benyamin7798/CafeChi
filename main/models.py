from django.db import models
from django.core.exceptions import ValidationError

def validate_ten_digits(amount):
    if amount>9999999999:
        raise ValidationError('The amount cannot have more than 10 digits.')
        


class Product(models.Model):

    HOT_DRINK = 'HD'
    COLD_DRINK = 'CD'
    CAKES = 'CAKES'

    PRODUCT_CHOICES = [
        (HOT_DRINK,'Hot Drink'),
        (COLD_DRINK,'Cold Drink'),
        (CAKES,'Cakes')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    sugar = models.IntegerField(validators=[validate_ten_digits])
    coffee = models.IntegerField(validators=[validate_ten_digits])
    flour = models.IntegerField(validators=[validate_ten_digits])
    chocolate = models.IntegerField(validators=[validate_ten_digits])

    vertical = models.CharField(max_length=10,
                                choices=PRODUCT_CHOICES,
                                default=CAKES)
    
    price = models.IntegerField(validators=[validate_ten_digits])
    
    #image = models.ImageField(upload_to='/static/images')

    def __str__(self):
        return self.name

    
    

