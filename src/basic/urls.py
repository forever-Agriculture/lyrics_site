"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from songs_artists.views import BandsListView, SongsListView, SongsDetailView, \
    SearchView, SongsCreateView, ArtistsCreateView, SongsUpdateView, \
    ArtistsUpdateView, SongsDeleteView, ArtistsDeleteView

urlpatterns = [

    # Bands
    url(r'^$', BandsListView.as_view(), name='home'),
    url(r'^bands/(?P<pk>\d+)/$', SongsListView.as_view(), name='bands'),
    url(r'^artist/add/$', ArtistsCreateView.as_view(), name='artist_add'),
    url(r'^artist/(?P<pk>\d+)/edit/$', ArtistsUpdateView.as_view(), name='artist_edit'),
    url(r'^artist/(?P<pk>\d+)/delete/$', ArtistsDeleteView.as_view(), name='artist_delete'),

    # Songs
    url(r'^texts/(?P<pk>\d+)/$', SongsDetailView.as_view(), name='texts'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^song/add/$', SongsCreateView.as_view(), name='song_add'),
    url(r'^song/(?P<pk>\d+)/edit/$', SongsUpdateView.as_view(), name='song_edit'),
    url(r'^song/(?P<pk>\d+)/delete/$', SongsDeleteView.as_view(), name='song_delete'),

    # Admin
    url(r'^admin/', admin.site.urls),

]
