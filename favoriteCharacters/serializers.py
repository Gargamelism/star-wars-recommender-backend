from rest_framework import serializers

from .models import FavoriteCharacters

class FavoriteCharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCharacters
        fields = ['user_id', 'favorite_characters']