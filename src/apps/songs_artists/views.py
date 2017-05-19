# -*- coding: utf-8 -*-

# django imports
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# app imports
from .models import Band, Lyrics


# Artists and bands
class BandsListView(ListView):
    """..."""
    template_name = 'main_page.html'
    model = Band
    context_object_name = 'bands_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(BandsListView, self).get_context_data(**kwargs)
        context['bands_range'] = range(context["paginator"].num_pages)
        return context


# Songs
class SongslistView(ListView):
    """..."""
    template_name = 'band.html'
    model = Lyrics
    context_object_name = 'songs_list'


# Songs
class SongsDetailView(DetailView):
    """..."""
    template_name = 'text.html'
    model = Lyrics
