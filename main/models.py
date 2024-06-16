from django.db import models
from django.core.validators import MaxValueValidator

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sugar = models.IntegerField(validators=[MaxValueValidator(9999999999)])

#class Image(models.Model):
  #  picture = models.ImageField()
   # description = models.CharField(max_length=255, blank=True)

   # def __str__(self):
    #    return self.description
