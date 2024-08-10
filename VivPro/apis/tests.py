from django.test import TestCase
from apis.models import SongInfo
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
# Create your tests here.

class SongViewTests(APITestCase):
    def setUp(self):
        self.data = {'song_id': '5vYA1mW9g2Cosdsdh1HUFUSmlb',
                    'title': '3AM',
                    'danceability': 0.521,
                    'energy': 0.673,
                    'mode': 1,
                    'acousticness': 0.00573,
                    'tempo': 108.031,
                    'duration_ms': 225947.0,
                    'num_sections': 8,
                    'num_segments': 830,
                    'star_rating': None}
        self.song = SongInfo.objects.create(**self.data)
        self.rating_url = reverse('add-rating', args=[self.song.song_id])
        self.list_url = reverse('song')

    def test_rate_song_success(self):
        self.assertEqual(self.song.star_rating, None)
        data = {'star_rating': 5}
        response = self.client.put(self.rating_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Rated the song successfully'})
        self.song.refresh_from_db()
        self.assertNotEqual(self.song.star_rating, 5)
    def test_list_song_success(self):
        response = self.client.get(self.list_url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)