from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from birds.models import Bird, Watch


def main_page(request):
    return render(request, 'birds/index.html')


class BirdsListView(ListView):
    model = Bird


class BirdsDetailView(DetailView):
    model = Bird


class WatchListView(ListView):
    model = Watch


class WatchDetailView(DetailView):
    model = Watch


class WatchCreateView(CreateView):
    model = Watch
    fields = ('bird', 'description', 'longitude', 'latitude', 'country', 'watched_at', 'author', 'is_private')
    success_url = reverse_lazy('events')
