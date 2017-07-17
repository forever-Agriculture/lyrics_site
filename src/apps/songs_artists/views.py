# django imports
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# app imports
from songs_artists.models import Band, Lyrics


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
class SongsListView(ListView):
    """Dynamic filtering"""
    template_name = 'band.html'
    context_object_name = 'song_list'

    def get_queryset(self):
        self.artist = get_object_or_404(Band, id=self.kwargs['pk'])
        return Lyrics.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SongsListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['artist'] = self.artist
        return context


class SongsDetailView(DetailView):
    """..."""
    template_name = 'text.html'
    model = Lyrics


# All songs
class SearchView(ListView):
    """..."""
    template_name = 'search.html'
    model = Lyrics
    context_object_name = 'songs_list'
