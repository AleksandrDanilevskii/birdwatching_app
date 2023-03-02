# Generated by Django 4.1.6 on 2023-02-11 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0006_alter_bird_created_at_alter_bird_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='infaclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='birds.infraclass'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bird',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 20, 22, 22, 601045), verbose_name='created at'),
        ),
    ]