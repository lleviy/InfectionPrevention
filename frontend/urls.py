from django.conf.urls import url
from django.urls import path, include

from frontend import views
from .views import SignUpView, ProfileView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]