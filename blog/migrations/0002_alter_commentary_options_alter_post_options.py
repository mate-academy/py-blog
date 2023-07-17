# Generated by Django 4.2.1 on 2023-07-11 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={
                "ordering": ["created_time"],
                "verbose_name_plural": "commentaries",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["created_time"], "verbose_name_plural": "posts"},
        ),
    ]
