# Generated by Django 5.1.1 on 2024-11-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_is_name_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_google',
            field=models.BooleanField(default=False),
        ),
    ]
