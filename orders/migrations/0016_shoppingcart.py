# Generated by Django 2.1.5 on 2020-04-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200427_1401'),
        ('orders', '0015_order_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('open', models.BooleanField(default=True)),
                ('product', models.ManyToManyField(to='menu.Product')),
            ],
        ),
    ]
