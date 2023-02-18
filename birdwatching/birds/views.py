from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from birds.forms import WatchModelForm
from birds.models import Bird, Watch


def main_page(request):
    return render(request, 'birds/index.html')


class BirdsListView(ListView):
    model = Bird


class BirdsDetailView(DetailView):
    model = Bird


class WatchListView(ListView):
    model = Watch

    def get_queryset(self):
        return Watch.objects.filter(is_private=False)


class WatchDetailView(DetailView):
    model = Watch


class WatchCreateView(CreateView):
    model = Watch
    # fields = ('bird', 'description', 'longitude', 'latitude', 'country', 'watched_at', 'author', 'is_private')
    form_class = WatchModelForm
    success_url = reverse_lazy('events')


class WatchUpdateView(UpdateView):
    model = Watch
    # fields = ('bird', 'description', 'longitude', 'latitude', 'country', 'watched_at', 'author', 'is_private')
    form_class = WatchModelForm
    success_url = reverse_lazy('events')


class WatchDeleteView(DeleteView):
    model = Watch
    success_url = reverse_lazy('events')
