from django.contrib import admin

from birds.models import (
    Bird,
    Infraclass,
    Order,
    Watch,
    Country,
)

admin.site.register(Bird)
admin.site.register(Infraclass)
admin.site.register(Order)
admin.site.register(Watch)
admin.site.register(Country)
