# Generated by Django 3.2.4 on 2021-06-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodItem",
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
                ("name", models.CharField(max_length=255)),
                ("calorie", models.FloatField()),
                ("created_at", models.DateField(auto_now=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
