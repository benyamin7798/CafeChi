from django.db import models
from django.core.exceptions import ValidationError

def max_integer_validator(amount):
    if amount>9999999999:
        raise Exception('')
    return True


class Product(models.Model):
    # برای اینکه بعدها در صورت نیاز، خواستیم نام ورتیکال را عوض کنیم اینطوری مینویسیم تا نیاز نباشد در همه جا نام آن را عوض کنیم
    HOT_DRINK = 'HOT DRINK'
    COLD_DRINK = 'COLD DRINK'
    CAKE = 'CAKE'
    ICE_CREAM = 'ICE CREAM'
    # لیست درست شده برای فیلد ورتیکال

    PRODUCT_CHOICES = [
        (HOT_DRINK, 'Hot Drink'),
        (COLD_DRINK, 'Cold Drink'),
        (CAKE, 'Cake'),
        (ICE_CREAM,'Ice Cream')
    ]

    #فیلدها
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sugar = models.IntegerField(validators=[max_integer_validator],default=0)
    Coffee = models.IntegerField(validators=[max_integer_validator],default=0)
    Flour = models.IntegerField(validators=[max_integer_validator],default=0)
    Chocolate = models.IntegerField(validators=[max_integer_validator],default=0)
    milk = models.IntegerField(validators=[max_integer_validator],default=0)
    vertical = models.CharField(max_length=10,choices=PRODUCT_CHOICES,default=HOT_DRINK)
    price = models.IntegerField(validators=[max_integer_validator],default=0)
    #تصویر در فایل آدرس داده شده ذخیره شده است. تنظیمات این آدرس در تنظیمات پروژه ایجاد گردیده است
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    #برای ثبت میزان فروش هر محصول از این فیلد غیرقابل دسترسی استفاده میکنیم
    sales_count = models.PositiveIntegerField(default=0,editable=False)

    # تابع برای چاپ خروجی
    def __str__(self):
        return self.name
    

class Warehouse(models.Model):
    #فیلدها
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

