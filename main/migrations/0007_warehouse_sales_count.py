# Generated by Django 5.0.6 on 2024-06-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_warehouse_sugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='sales_count',
            field=models.IntegerField(default=0),
        ),
    ]