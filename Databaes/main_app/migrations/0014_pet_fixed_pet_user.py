# Generated by Django 5.0.1 on 2024-01-22 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_remove_pet_fixed_remove_pet_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='fixed',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]