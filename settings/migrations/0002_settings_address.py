# Generated by Django 4.2.9 on 2024-02-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="address",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
