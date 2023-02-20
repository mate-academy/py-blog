# Generated by Django 4.1 on 2023-02-20 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_commentary_options_alter_commentary_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentary',
            options={'ordering': ['-created_time'], 'verbose_name_plural': 'commentaries'},
        ),
        migrations.AlterField(
            model_name='commentary',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaries', to='blog.post'),
        ),
    ]
