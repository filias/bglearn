# Generated by Django 5.0.3 on 2024-03-29 18:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("category", models.CharField(max_length=32)),
                ("position", models.ImageField(upload_to="positions/")),
                ("solution", models.ImageField(upload_to="positions/")),
                ("source", models.CharField(max_length=255)),
            ],
        ),
    ]