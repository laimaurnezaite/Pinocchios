# Generated by Django 2.1.5 on 2020-04-27 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200427_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
