# Generated by Django 4.1 on 2023-11-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_created_at_post_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentary',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
