# Generated by Django 5.1.3 on 2024-11-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='work_time',
            field=models.TextField(default='00:00:00:00', max_length=200, null=True),
        ),
    ]