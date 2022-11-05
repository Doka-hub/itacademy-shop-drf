from django.urls import path, include

from rest_framework.authtoken.views import ObtainAuthToken

from .views import RegisterAPIView


urlpatterns = [
    path('auth/', ObtainAuthToken.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
