from django.contrib import admin
from django.urls import path

from birds.views import (
    main_page,
    BirdsListView, BirdsDetailView,
    WatchListView, WatchDetailView, WatchCreateView, WatchUpdateView, WatchDeleteView,
)

urlpatterns = [
    path('', main_page),
    path('birds/', BirdsListView.as_view(), name='birds'),
    path('bird/<int:pk>', BirdsDetailView.as_view(), name='bird'),
    path('events/', WatchListView.as_view(), name='events'),
    path('event/<int:pk>', WatchDetailView.as_view(), name='event'),
    path('events/create', WatchCreateView.as_view(), name='event_create'),
    path('events/update/<int:pk>', WatchUpdateView.as_view(), name='event_update'),
    path('events/delete/<int:pk>', WatchDeleteView.as_view(), name='event_delete'),
    path('admin/', admin.site.urls),
]
