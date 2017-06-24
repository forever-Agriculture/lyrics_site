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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.songs_artists.views import BandsListView, SongsListView, SongsDetailView, SearchView
# from apps.songs_artists import views

urlpatterns = [

    # Bands
    url(r'^$', BandsListView.as_view(), name='home'),
    url(r'^bands/(?P<pk>\d+)/$', SongsListView.as_view(), name='bands'),

    # Songs
    url(r'^texts/(?P<pk>\d+)/$', SongsDetailView.as_view(), name='texts'),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Search
    url(r'^search/$', SearchView.as_view(), name='search'),

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static\
    (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
