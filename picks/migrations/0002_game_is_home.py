# Generated by Django 4.2.18 on 2025-02-10 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game", name="is_home", field=models.BooleanField(default=True),
        ),
    ]
