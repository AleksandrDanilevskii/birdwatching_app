from django.contrib import admin
from django.urls import path

from birds.views import main_page, BirdsListView, BirdsDetailView

urlpatterns = [
    path('', main_page),
    path('birds/', BirdsListView.as_view(), name='birds'),
    path('bird/<int:pk>', BirdsDetailView.as_view(), name='bird'),
    path('admin/', admin.site.urls),
]
