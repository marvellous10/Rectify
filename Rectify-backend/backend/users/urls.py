from django.urls import path
from .views import *

urlpatterns = [
    path('spotify/login/', SpotifyLoginView.as_view(), name='spotify_login'),
    path('spotify/callback/', SpotifyCallBackView.as_view(), name='spotify_callback'),
    path('spotify/testcode/', GetCodeQuery.as_view(), name='spotify_getcode'),
    path('spotify/deletesession/', DeleteSession.as_view(), name='spotify_deletesession'),
    path('spotify/getsession/', GetSessions.as_view(), name='spotify_getsession'),
]