# django imports
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, \
                                                        DeleteView
from django.views.generic.detail import DetailView

# app imports
from songs_artists.models import Band, Lyrics


# Artists
class BandsListView(ListView):
    """Main page view"""
    template_name = 'main_page.html'
    model = Band
    context_object_name = 'bands_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(BandsListView, self).get_context_data\
                                            (**kwargs)
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
        context = super(SongsListView, self).get_context_data\
                                                (**kwargs)
        # Add in the publisher
        context['artist'] = self.artist
        return context


class ArtistsCreateView(CreateView):
    """Creating an artist"""
    template_name = 'add_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)


class ArtistsUpdateView(UpdateView):
    """Editing an artist"""
    template_name = 'edit_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)


class ArtistsDeleteView(DeleteView):
    """Deleting an artist"""
    template_name = 'delete_artist.html'
    model = Band
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)


# Songs
class SongsDetailView(DetailView):
    """Lyrics"""
    template_name = 'text.html'
    model = Lyrics


class SongsCreateView(CreateView):
    """Creating a song"""
    template_name = 'add_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SongsCreateView, self).get_context_data\
                                                    (**kwargs)
        context['artists'] = Band.objects.all()
        return context


class SongsUpdateView(UpdateView):
    """Editing a song"""
    template_name = 'edit_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SongsUpdateView, self).get_context_data\
                                                (**kwargs)
        context['artists'] = Band.objects.all()
        return context


class SongsDeleteView(DeleteView):
    """Deleting a song"""
    template_name = 'delete_song.html'
    model = Lyrics
    fields = '__all__'

    def get_success_url(self):
        return reverse('search')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(self.__class__, self).post\
                    (request, *args, **kwargs)


# Search
class SearchView(ListView):
    """All songs view"""
    template_name = 'search.html'
    model = Lyrics
    context_object_name = 'songs_list'
