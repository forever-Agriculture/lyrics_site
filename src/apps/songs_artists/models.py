from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Band(models.Model):
    """music band model"""
    band_name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=_("Artist"))

    photo = models.ImageField(
        blank=True,
        verbose_name=_("Picture"),
        null=True)

    notes = models.TextField(
        blank=True,
        verbose_name=_("Extra notes"))

    # song = models.ManyToManyField('Lyrics',
    #     blank=True,
    #     verbose_name=_("Song"))

    class Meta(object):
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    def __str__(self):
        return self.band_name


class Lyrics(models.Model):
    """song model"""
    song_name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=_("Song name"))

    song_lyrics = models.TextField(
        blank=False,
        verbose_name=_("Lyrics"))

    artist = models.ForeignKey('Band',
        verbose_name=_("Artist"),
        # related_name="songs",
        blank=False,
        # null=True,
        on_delete=models.PROTECT)

    class Meta(object):
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        if self.artist:
            return u'{} {}'.format(self.song_name, self.artist.band_name)
        else:
            return u'{}'.format(self.song_name)
