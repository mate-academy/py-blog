# Generated by Django 4.2 on 2024-09-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_created_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]