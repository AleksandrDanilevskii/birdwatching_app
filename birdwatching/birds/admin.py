from django.contrib import admin

from birds.models import (
    Bird,
    Infraclass,
    Order,
)

admin.site.register(Bird)
admin.site.register(Infraclass)
admin.site.register(Order)

