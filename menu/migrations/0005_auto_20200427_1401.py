# Generated by Django 2.1.5 on 2020-04-27 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200424_1546'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FreeToppings',
        ),
        migrations.DeleteModel(
            name='MainDish',
        ),
        migrations.DeleteModel(
            name='Toppings',
        ),
    ]