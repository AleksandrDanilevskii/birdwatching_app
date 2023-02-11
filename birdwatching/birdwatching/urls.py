from django.contrib import admin
from django.urls import path

from birds.views import main_page

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
]
