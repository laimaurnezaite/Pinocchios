# Generated by Django 2.1.5 on 2020-04-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_product_number_of_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('unit_price', models.FloatField(blank=True, null=True)),
                ('item_category', models.CharField(max_length=255)),
            ],
        ),
    ]