# Generated by Django 4.1.6 on 2023-02-18 12:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0017_alter_bird_created_at_alter_watch_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='bird',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='birds.bird'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 12, 36, 33, 670432), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 12, 36, 33, 670987), verbose_name='created at'),
        ),
    ]
