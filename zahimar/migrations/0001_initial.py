# Generated by Django 4.2 on 2023-04-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ZahimarImagePrediction",
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
                ("image", models.ImageField(upload_to="zahimar/")),
                ("classes", models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                "verbose_name_plural": "Zahimar Image Prediction",
            },
        ),
    ]
