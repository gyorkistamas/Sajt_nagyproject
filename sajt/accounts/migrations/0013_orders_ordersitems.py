# Generated by Django 5.1.1 on 2024-12-09 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_customuser_is_authenticated'),
        ('itemManager', '0002_createproductqueue_reason_createproductqueue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(blank=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.orders')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itemManager.product')),
            ],
        ),
    ]
