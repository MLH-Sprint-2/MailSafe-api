from django.urls import path, include
from . views import get_aliases, get_domains, get_alias_filtered
urlpatterns = [
    path('alias', get_aliases, name="get_aliases"),
    path('domains', get_domains, name="get_domains"),
    path('alias/<str:DOMAIN>',
         get_alias_filtered, name="get_alias_filtered"),
]
