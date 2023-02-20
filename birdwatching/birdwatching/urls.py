from django.contrib import admin
from django.urls import path

from birds.views import (
    main_page,
    BirdsListView, BirdsDetailView,
    WatchListView, WatchDetailView, WatchCreateView, WatchUpdateView, WatchDeleteView,
    MyWatchListView,
)
from users.views import RegistrationView, UserLoginView, UserLogoutView, UserTemplateView

urlpatterns = [
    path('', main_page),
    # birds
    path('birds/', BirdsListView.as_view(), name='birds'),
    path('bird/<int:pk>/', BirdsDetailView.as_view(), name='bird'),
    path('events/my/', MyWatchListView.as_view(), name='my_events'),
    path('events/', WatchListView.as_view(), name='events'),
    path('event/<int:pk>/', WatchDetailView.as_view(), name='event'),
    path('events/create/', WatchCreateView.as_view(), name='event_create'),
    path('events/update/<int:pk>/', WatchUpdateView.as_view(), name='event_update'),
    path('events/delete/<int:pk>/', WatchDeleteView.as_view(), name='event_delete'),
    # users
    path('users/create/', RegistrationView.as_view(), name='registration'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/logout/', UserLogoutView.as_view(), name='logout'),
    path('users/my-account/', UserTemplateView.as_view(), name='my_account'),

    # other
    path('admin/', admin.site.urls),
]
