# Generated by Django 4.2.9 on 2024-01-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_name", models.CharField(max_length=50)),
                ("logo", models.ImageField(upload_to="settings/")),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("description", models.TextField(max_length=300)),
                ("fb_link", models.URLField()),
                ("twitter_link", models.URLField()),
                ("instagram_link", models.URLField()),
            ],
        ),
    ]