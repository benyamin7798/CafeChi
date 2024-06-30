# Generated by Django 5.0.6 on 2024-06-21 15:00

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Chocolate',
            field=models.IntegerField(default=0, validators=[main.models.max_integer_validator]),
        ),
        migrations.AddField(
            model_name='product',
            name='Coffee',
            field=models.IntegerField(default=0, validators=[main.models.max_integer_validator]),
        ),
        migrations.AddField(
            model_name='product',
            name='Flour',
            field=models.IntegerField(default=0, validators=[main.models.max_integer_validator]),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, validators=[main.models.max_integer_validator]),
        ),
        migrations.AddField(
            model_name='product',
            name='vertical',
            field=models.CharField(choices=[('HD', 'Hot Drink'), ('CD', 'Cold Drink'), ('CAKE', 'Cake'), ('IC', 'Ice Cream')], default='HD', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sugar',
            field=models.IntegerField(default=0, validators=[main.models.max_integer_validator]),
        ),
    ]
