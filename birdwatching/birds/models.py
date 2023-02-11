import datetime

from django.db import models


class Infraclass(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', max_length=2000, null=True, blank=True)
    infaclass = models.ForeignKey(Infraclass, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} ({self.infaclass.name})'


class Bird(models.Model):
    # objects = models.Manager()
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    name_latin = models.CharField(verbose_name='name latin', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='created at', default=datetime.datetime.now())
    updated_at = models.DateTimeField(verbose_name='updated at', null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'
# Meta =
