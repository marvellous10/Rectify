from django.urls import path
from .views import *

urlpatterns = [
    path('spotify/login/', SpotifyLoginView.as_view(), name='spotify_login'),
    path('spotify/callback/', SpotifyCallBackView.as_view(), name='spotify_callback'),
    #path('spotify/testcode/', GetCodeQuery.as_view(), name='spotify_getcode'), #For debug, edit the view code
    path('spotify/deletesession/', DeleteSession.as_view(), name='spotify_deletesession'), #For debug, edit the view code
    path('spotify/getsession/', GetSessions.as_view(), name='spotify_getsession'), #For debug, edit the view code
]