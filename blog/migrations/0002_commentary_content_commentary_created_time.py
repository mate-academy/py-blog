# Generated by Django 4.1 on 2023-11-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentary",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="commentary",
            name="created_time",
            field=models.DateTimeField(null=True),
        ),
    ]