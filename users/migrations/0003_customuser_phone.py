# Generated by Django 5.2.1 on 2025-06-28 16:58

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[users.models.validate_phone_number], verbose_name='Phone'),
        ),
    ]
