from rest_framework.routers import DefaultRouter

from favoriteCharacters.views import FavoriteCharactersViewSet

# must be first call
router = DefaultRouter(trailing_slash=False)

router.register(r'favorite-characters/?', FavoriteCharactersViewSet, basename='favorite-characters')

# must be last call
urlpatterns = router.urls