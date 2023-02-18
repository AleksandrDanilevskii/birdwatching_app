from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
