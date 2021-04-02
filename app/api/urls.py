from django.urls import path, include
from . views import get_aliases
urlpatterns = [
    path('aliases', get_aliases, name="get_aliases"),
]
