# Generated by Django 2.1.5 on 2020-05-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='Cambridge', max_length=255),
        ),
    ]
