# Generated by Django 4.1 on 2023-03-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_commentary_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]