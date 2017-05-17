# -*- coding: utf-8 -*-

# django imports
from django.contrib.postgres.search import SearchVector
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
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(BandsListView, self).get_context_data(**kwargs)
        context['bands_range'] = range(context["paginator"].num_pages)
        return context


class BandsDetailView(ListView):
    """..."""
    template_name = 'band.html'
    model = Lyrics
    context_object_name = 'songs_list'


# Songs
class SongsListView(ListView):
    """..."""
    template_name = 'band.html'
    model = Lyrics
    context_object_name = 'songs_list'

    # def get_context_data(self, **kwargs):
    #     context = super(SongsListView, self).get_context_data(**kwargs)
    #     context['search'] = Lyrics.objects.annotate(search=SearchVector('song_name', 'artist'),
    #                                                 ).filter(search=search_field)
    #     return context


class SongsDetailView(DetailView):
    """..."""
    template_name = 'text.html'
    model = Lyrics
