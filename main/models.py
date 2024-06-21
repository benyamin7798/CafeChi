from django.db import models

def max_integer_validator(amount):
    if amount>9999999999:
        return False
    return True


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sugar = models.IntegerField(validators=[max_integer_validator])
    sugar = models.IntegerField(validators=[max_integer_validator])
    sugar = models.IntegerField(validators=[max_integer_validator])
    

