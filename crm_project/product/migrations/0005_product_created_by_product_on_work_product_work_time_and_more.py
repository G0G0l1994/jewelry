# Generated by Django 5.1.3 on 2024-11-25 08:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_name_alter_product_status_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='on_work',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='work_time',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'принят'), ('2', 'в работе'), ('4', 'правки'), ('3', 'согласование'), ('5', 'на росте'), ('6', 'выполнен')], max_length=20, null=True),
        ),
    ]
