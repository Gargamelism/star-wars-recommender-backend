import json

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import FavoriteCharacters

class FavoriteCharactersTests(APITestCase):
    def test_create(self):
        url = reverse('favorite-characters-list')
        response = self.client.post(url)
        userId = json.loads(response.content)['userid']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FavoriteCharacters.objects.count(), 1)
        self.assertEqual(FavoriteCharacters.objects.get().user_id, userId)

    def test_update(self):
        createUrl = reverse('favorite-characters-list')
        response = self.client.post(createUrl)
        userId = json.loads(response.content)['userid']
        
        updateUrl = reverse('favorite-characters-detail', args=[userId])
        self.client.patch(updateUrl, {'user_id': userId, 'favorite_characters': json.dumps(['1', '2'])})
        self.assertEqual(FavoriteCharacters.objects.get(pk=userId).favorite_characters, ['1', '2'])

    def test_retrieve(self):
        createUrl = reverse('favorite-characters-list')
        response = self.client.post(createUrl)
        userId = json.loads(response.content)['userid']
        
        userUrl = reverse('favorite-characters-detail', args=[userId])

        self.client.patch(userUrl, {'user_id': userId, 'favorite_characters': json.dumps(['1', '2'])})
        
        response = self.client.get(userUrl, {'user_id': userId, 'favorite_characters': json.dumps(['1', '2'])})
        response = json.loads(response.content)
        
        self.assertEqual(response['user_id'], userId)
        self.assertEqual(response['favorite_characters'], ['1', '2'])