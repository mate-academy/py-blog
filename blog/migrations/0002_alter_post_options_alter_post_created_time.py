# Generated by Django 4.1 on 2023-03-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_time"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
