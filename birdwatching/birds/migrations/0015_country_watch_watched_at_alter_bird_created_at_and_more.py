# Generated by Django 4.1.6 on 2023-02-12 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0014_watch_author_alter_bird_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='watch',
            name='watched_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 6, 42, 28, 816260), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 6, 42, 28, 816802), verbose_name='created at'),
        ),
    ]
