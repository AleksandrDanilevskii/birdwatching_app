from django.contrib import admin
from django.urls import path

from birds.views import (
    main_page,
    BirdsListView, BirdsDetailView,
    WatchListView, WatchDetailView,
)

urlpatterns = [
    path('', main_page),
    path('birds/', BirdsListView.as_view(), name='birds'),
    path('bird/<int:pk>', BirdsDetailView.as_view(), name='bird'),
    path('events/', WatchListView.as_view(), name='events'),
    path('event/<int:pk>', WatchDetailView.as_view(), name='event'),
    path('admin/', admin.site.urls),
]
