# from django.test import TestCase
# from songs_artists.models import Band, Lyrics
#
#
# # Testing models
# class BandTest(TestCase):
#     """Testing Band model"""
#
#     def create_band(self, band_name="just a test artist"):
#         return Band.objects.create(band_name=band_name)
#
#     def test_band_creation(self):
#         b = self.create_band()
#         self.assertTrue(isinstance(b, Band))
#         self.assertEqual(b.__unicode__(), b.band_name)
#
#
# class LyricsTest(TestCase):
#     """Testing Lyrics model"""
#
#     def create_lyrics(self, song_name="just a test song", song_lyrics="test song lyrics"):
#         return Lyrics.objects.create(song_name=song_name, song_lyrics=song_lyrics)
#
#     def test_band_creation(self):
#         l = self.create_lyrics()
#         self.assertTrue(isinstance(l, Lyrics))
#         self.assertEqual(l.__unicode__(), l.song_name)
#
#
# # Testing views
# # No idea
