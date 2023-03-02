# Generated by Django 4.1.6 on 2023-02-18 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0022_alter_bird_created_at_alter_watch_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 15, 38, 49, 590412, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 15, 38, 49, 590981, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 18, 15, 38, 49, 590987, tzinfo=datetime.timezone.utc), null=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='watched_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 15, 38, 49, 590970, tzinfo=datetime.timezone.utc), verbose_name='watched at'),
        ),
    ]
