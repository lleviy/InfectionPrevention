from django.conf.urls import url
from django.urls import path, include

from .views import ProfileAPIView


urlpatterns = [
    path('profile/', ProfileAPIView.as_view(), name='user_profile'),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
