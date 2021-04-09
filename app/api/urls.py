from django.urls import path, include
from . import views
# Router for DRF viewSet
from rest_framework.routers import DefaultRouter
# Make a default router
router = DefaultRouter()
# Register the new router
router.register(r'users', views.AliasesViewSet, basename='users')
urlpatterns = [
    path('alias', views.get_aliases, name="get_aliases"),
    path('domains', views.get_domains, name="get_domains"),
    path('alias/<str:DOMAIN>',
         views.get_alias_filtered, name="get_alias_filtered"),
    path('alias/<str:DOMAIN>/<str:ID>',
         views.delete_alias, name="delete_alias"),
    path('', include(router.urls))
]
