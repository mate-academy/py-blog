# Generated by Django 4.2.7 on 2023-11-20 16:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={
                "ordering": ("post",),
                "verbose_name": "Commentary",
                "verbose_name_plural": "Commentaries",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("title",)},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ("username",)},
        ),
    ]