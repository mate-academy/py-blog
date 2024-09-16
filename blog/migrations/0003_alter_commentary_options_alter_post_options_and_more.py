# Generated by Django 4.1 on 2023-05-27 21:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_commentary_created_time_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={"ordering": ["created_time"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["created_time"]},
        ),
        migrations.RenameField(
            model_name="post",
            old_name="content",
            new_name="contents",
        ),
    ]
