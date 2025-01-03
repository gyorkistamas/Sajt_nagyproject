# Generated by Django 5.1.1 on 2024-12-01 10:46

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSession',
            fields=[
                ('session_key', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('session_data', models.JSONField(default=dict)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expire_at', models.DateTimeField(default=datetime.datetime(2024, 12, 8, 10, 46, 25, 259337, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
