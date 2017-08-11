# django imports
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, \
                                                        DeleteView
from django.views.generic.detail import DetailView

# app imports
from songs_artists.tools import CancelButtonMixin
from songs_artists.models import Band, Lyrics


# Artists
class BandsListView(ListView):
    """Main page view"""
    template_name = 'main_page.html'
    model = Band
    context_object_name = 'bands_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bands_range'] = range(context["paginator"].num_pages)
        return context


class SongsListView(ListView):
    """Dynamic filtering"""
    template_name = 'band.html'
    context_object_name = 'song_list'

    def get_queryset(self):
        self.artist = get_object_or_404(Band, id=self.kwargs['pk'])
        return Lyrics.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['artist'] = self.artist
        return context


class ArtistsCreateView(CancelButtonMixin, CreateView):
    """Creating an artist"""
    template_name = 'add_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')


class ArtistsUpdateView(CancelButtonMixin, UpdateView):
    """Editing an artist"""
    template_name = 'edit_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')


class ArtistsDeleteView(CancelButtonMixin, DeleteView):
    """Deleting an artist"""
    template_name = 'delete_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')


# Songs
class SongsDetailView(DetailView):
    """Lyrics"""
    template_name = 'text.html'
    model = Lyrics


class SongsCreateView(CancelButtonMixin, CreateView):
    """Creating a song"""
    template_name = 'add_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Band.objects.all()
        return context


class SongsUpdateView(CancelButtonMixin, UpdateView):
    """Editing a song"""
    template_name = 'edit_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Band.objects.all()
        return context


class SongsDeleteView(CancelButtonMixin, DeleteView):
    """Deleting a song"""
    template_name = 'delete_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')


# Search
class SearchView(ListView):
    """All songs view"""
    template_name = 'search.html'
    model = Lyrics
    context_object_name = 'songs_list'
