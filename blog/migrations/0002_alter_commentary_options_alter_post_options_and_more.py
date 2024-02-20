# Generated by Django 4.1.3 on 2022-12-07 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={"ordering": ["created_time"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_time"]},
        ),
        migrations.AlterField(
            model_name="commentary",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="commentaries",
                to="blog.post",
            ),
        ),
    ]
