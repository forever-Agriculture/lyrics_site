# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from djrichtextfield.models import RichTextField
from django.db import models


class Band(models.Model):
    """music band model"""
    band_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Назва виконавця")

    photo = models.ImageField(
        blank=True,
        verbose_name="Зображення",
        null=True)

    notes = models.TextField(
        blank=True,
        verbose_name="Додаткові нотатки")

    song = models.ManyToManyField('Lyrics',
        blank=True,
        verbose_name="Пісенька")

    class Meta(object):
        verbose_name = "Виконавець"
        verbose_name_plural = "Виконавці"

    def __str__(self):
        return self.band_name


class Lyrics(models.Model):
    """song model"""
    song_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Назва пісні")

    song_lyrics = RichTextField(
        blank=False,
        verbose_name="Текст пісні")

    artist = models.ForeignKey('Band',
        verbose_name='Виконавець',
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    class Meta(object):
        verbose_name = "Пісенька"
        verbose_name_plural = "Пісеньки"

    def __str__(self):
        if self.artist:
            return u'{} {}'.format(self.song_name, self.artist.band_name)
        else:
            return u'{}'.format(self.song_name)
