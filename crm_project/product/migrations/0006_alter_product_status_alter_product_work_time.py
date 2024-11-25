# Generated by Django 5.1.3 on 2024-11-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_created_by_product_on_work_product_work_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'принят'), ('2', 'в работе'), ('4', 'правки'), ('3', 'согласование'), ('5', 'на росте'), ('6', 'выполнен')], default='1', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='work_time',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]