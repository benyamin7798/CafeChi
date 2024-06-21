from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
def max_integer_validator(amount):
    if amount>9999999999:
        raise Exception('')
    return True


class Product(models.Model):

    HOT_DRINK = 'HD'
    COLD_DRINK = 'CD'
    CAKE = 'CAKE'
    ICE_CREAM = 'IC'

    PRODUCT_CHOICES = [
        (HOT_DRINK, 'Hot Drink'),
        (COLD_DRINK, 'Cold Drink'),
        (CAKE, 'Cake'),
        (ICE_CREAM,'Ice Cream')
    ]


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sugar = models.IntegerField(validators=[max_integer_validator],default=0)
    Coffee = models.IntegerField(validators=[max_integer_validator],default=0)
    Flour = models.IntegerField(validators=[max_integer_validator],default=0)
    Chocolate = models.IntegerField(validators=[max_integer_validator],default=0)
    milk = models.IntegerField(validators=[max_integer_validator],default=0)
    vertical = models.CharField(max_length=10,choices=PRODUCT_CHOICES,default=HOT_DRINK)
    price = models.IntegerField(validators=[max_integer_validator],default=0)

    image = models.ImageField(upload_to='product_images',blank=True,null=True)


    def __str__(self):
        return self.name
    

