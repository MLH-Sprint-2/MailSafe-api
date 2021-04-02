from django.urls import path, include
from . views import get_aliases, get_domains
urlpatterns = [
    path('aliases', get_aliases, name="get_aliases"),
    path('domains', get_domains, name="get_domains"),
]
