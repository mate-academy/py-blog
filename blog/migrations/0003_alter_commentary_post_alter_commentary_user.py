# Generated by Django 5.0.3 on 2024-03-08 20:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_user_options_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_commentary",
                to="blog.post",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_commentary",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
