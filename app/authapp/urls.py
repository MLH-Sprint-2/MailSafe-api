from django.urls import path, include
from authapp import views
from api.views import TokenObtainView
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('users/token/email/', TokenObtainView.as_view())

]
