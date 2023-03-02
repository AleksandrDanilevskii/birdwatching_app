# Generated by Django 4.1.6 on 2023-02-19 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0031_infraclass_created_at_infraclass_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='updated at'),
        ),
    ]