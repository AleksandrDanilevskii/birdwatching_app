# Generated by Django 4.1.6 on 2023-02-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0026_alter_watch_watched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='watched_at',
            field=models.DateField(verbose_name='watched at'),
        ),
    ]
