# Generated by Django 4.1 on 2024-02-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_commentary_post'),
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
