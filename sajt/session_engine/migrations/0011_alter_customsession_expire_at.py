# Generated by Django 5.1.1 on 2024-12-09 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_engine', '0010_alter_customsession_expire_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsession',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 16, 14, 11, 33, 158363, tzinfo=datetime.timezone.utc)),
        ),
    ]
