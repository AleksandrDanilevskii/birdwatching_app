# Generated by Django 4.1.6 on 2023-02-11 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0007_order_infaclass_alter_bird_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 20, 25, 46, 843133), verbose_name='created at'),
        ),
    ]
