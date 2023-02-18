# from django.contrib.gis.db.models import PointField
# from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()


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
    created_at = models.DateTimeField(verbose_name='created at', default=now)
    updated_at = models.DateTimeField(verbose_name='updated at', null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


# Meta =
class Country(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Watch(models.Model):
    # objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_private = models.BooleanField(verbose_name='is private', default=False)
    description = models.TextField(verbose_name='description', max_length=500, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    watched_at = models.DateTimeField(verbose_name='watched at', default=now)
    created_at = models.DateTimeField(verbose_name='created at', default=now)
    updated_at = models.DateTimeField(verbose_name='updated at', null=True, blank=True, default=now)
    bird = models.ForeignKey(Bird, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.bird} ({self.country}, {self.watched_at})'
