# Generated by Django 2.1.5 on 2020-04-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200427_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_toppings',
            field=models.IntegerField(default=0),
        ),
    ]
