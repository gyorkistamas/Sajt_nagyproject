# Generated by Django 5.1.1 on 2024-12-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_selected_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
