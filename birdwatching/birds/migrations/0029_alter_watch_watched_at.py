# Generated by Django 4.1.6 on 2023-02-18 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0028_alter_watch_watched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='watched_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='watched at'),
        ),
    ]
