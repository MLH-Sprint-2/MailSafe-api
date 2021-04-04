from django.urls import path, include
from . views import get_aliases, get_domains, get_alias_filtered
urlpatterns = [
    path('aliases', get_aliases, name="get_aliases"),
    path('aliases/domains', get_domains, name="get_domains"),
    path('aliases/domains/<str:DOMAIN>',
         get_alias_filtered, name="get_alias_filtered"),


]
