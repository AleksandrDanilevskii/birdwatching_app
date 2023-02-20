from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class MyWatchListView(LoginRequiredMixin, ListView):
    model = Watch

    def get_queryset(self):
        return Watch.objects.filter(author=self.request.user)


class WatchDetailView(DetailView):
    model = Watch


class WatchCreateView(LoginRequiredMixin, CreateView):
    model = Watch
    form_class = WatchModelForm
    success_url = reverse_lazy('events')


class WatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Watch
    form_class = WatchModelForm
    success_url = reverse_lazy('events')

    def test_func(self):
        return self.get_object().author == self.request.user


class WatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Watch
    success_url = reverse_lazy('events')

    def test_func(self):
        return self.get_object().author == self.request.user
