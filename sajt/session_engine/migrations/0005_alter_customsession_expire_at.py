# Generated by Django 5.1.1 on 2024-12-02 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_engine', '0004_alter_customsession_expire_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsession',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 9, 15, 8, 41, 371905, tzinfo=datetime.timezone.utc)),
        ),
    ]
