# Generated by Django 5.1.3 on 2024-11-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_start_date_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('принят', 'принят'), ('в работе', 'в работе'), ('правки', 'правки'), ('согласование', 'согласование'), ('на росте', 'на росте'), ('выполнен', 'выполнен')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.CharField(choices=[('повеска', 'подвеска'), ('кольцо', 'кольцо'), ('брошь', 'брошь'), ('серьги', 'серьги'), ('комплект', 'комплект'), ('пусеты', 'пусеты'), ('другое', 'другое'), ('колье', 'колье'), ('браслет', 'браслет')], default='кольцо', max_length=30),
        ),
    ]
