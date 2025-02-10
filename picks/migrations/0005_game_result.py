# Generated by Django 4.2.18 on 2025-02-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picks", "0004_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="result",
            field=models.CharField(
                blank=True,
                choices=[("W", "Win"), ("L", "Loss")],
                help_text="Enter 'W' if the team won or 'L' if the team lost.",
                max_length=1,
                null=True,
            ),
        ),
    ]
