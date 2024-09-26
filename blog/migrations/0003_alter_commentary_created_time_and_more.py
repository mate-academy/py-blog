# Generated by Django 4.2.5 on 2023-09-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_commentary_options_alter_post_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
