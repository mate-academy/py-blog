# Generated by Django 4.1 on 2024-03-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_commentary_content_alter_commentary_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]