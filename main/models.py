from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
def max_integer_validator(amount):
    if amount>9999999999:
        raise Exception('')
    return True


class Product(models.Model):

    HOT_DRINK = 'HOT DRINK'
    COLD_DRINK = 'COLD DRINK'
    CAKE = 'CAKE'
    ICE_CREAM = 'ICE CREAM'

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

    sales_count = models.PositiveIntegerField(default=0,editable=False)


    def __str__(self):
        return self.name
    

class Warehouse(models.Model):
    sugar = models.IntegerField(default=0)
    coffee = models.IntegerField(default=0)
    flour = models.IntegerField(default=0)
    chocolate = models.IntegerField(default=0)
    milk = models.IntegerField(default=0)

    # مطمئن میشود که فقط یک نمونه از کلاس انبار، ساخته شده است
    def save(self, *args, **kwargs):
        if Warehouse.objects.exists() and not self.pk:
            raise ValidationError('There can be only one Warehouse instance.')
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'Warehouse'

