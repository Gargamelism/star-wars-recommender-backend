from django.db import models

class FavoriteCharacters(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    favorite_characters = models.JSONField(encoder=None, decoder=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.favorite_characters