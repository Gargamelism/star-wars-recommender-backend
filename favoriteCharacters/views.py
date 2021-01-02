from django.http import JsonResponse
from django.utils.crypto import get_random_string
from rest_framework import viewsets, status
from rest_framework.decorators import action

import os

from .models import FavoriteCharacters
from .serializers import FavoriteCharactersSerializer

class FavoriteCharactersViewSet(viewsets.ModelViewSet):
    queryset = FavoriteCharacters.objects.all()
    serializer_class = FavoriteCharactersSerializer

    def create(self, request):
        userId = get_random_string(length=32)
        FavoriteCharacters(user_id = userId, favorite_characters = []).save()

        return JsonResponse({
            'userid': userId
        },
        status=status.HTTP_201_CREATED)