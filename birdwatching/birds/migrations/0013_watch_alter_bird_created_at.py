# Generated by Django 4.1.6 on 2023-02-12 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0012_bird_order_alter_bird_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.BooleanField(default=False, verbose_name='is private')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 2, 12, 6, 29, 14, 46386), verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='updated at')),
            ],
        ),
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 6, 29, 14, 46055), verbose_name='created at'),
        ),
    ]
