# Generated by Django 4.1 on 2023-11-18 23:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_commentary_created_time_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={"ordering": ("created_time",)},
        ),
    ]
