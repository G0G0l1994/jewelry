# Generated by Django 5.1.3 on 2024-11-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
