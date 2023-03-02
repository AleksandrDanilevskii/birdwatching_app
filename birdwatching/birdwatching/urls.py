from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from birds.views import (
    main_page,
    BirdsListView, BirdsDetailView,
    WatchListView, WatchDetailView, WatchCreateView, WatchUpdateView, WatchDeleteView,
    MyWatchListView,
)
from users.views import (
    RegistrationView,
    UserLoginView,
    UserLogoutView,
    UserTemplateView,
    UserDetailView,
    UserUpdateView,
)


urlpatterns = [
    path('', main_page),
    # birds
    path('birds/', BirdsListView.as_view(), name='birds'),
    path('birds/<int:pk>/', BirdsDetailView.as_view(), name='bird'),
    path('events/my/', MyWatchListView.as_view(), name='my_events'),
    path('events/', WatchListView.as_view(), name='events'),
    path('events/<int:pk>/', WatchDetailView.as_view(), name='event'),
    path('events/create/', WatchCreateView.as_view(), name='event_create'),
    path('events/update/<int:pk>/', WatchUpdateView.as_view(), name='event_update'),
    path('events/delete/<int:pk>/', WatchDeleteView.as_view(), name='event_delete'),
    # users
    path('users/create/', RegistrationView.as_view(), name='registration'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/logout/', UserLogoutView.as_view(), name='logout'),
    path('users/my-account/', UserTemplateView.as_view(), name='my_account'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='account'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/change_password/<int:pk>/', PasswordChangeView.as_view(), name='change_password'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),


    # other
    path('admin/', admin.site.urls),
]
