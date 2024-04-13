import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dotenv import load_dotenv


load_dotenv()

class SpotifyLoginView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        client_ID = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        scope = 'user-read-private user-read-email'
        
        sp_oauth = SpotifyOAuth(client_ID, client_secret, redirect_uri, scope=scope)
        auth_url = sp_oauth.get_authorize_url()
        
        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)
    
class SpotifyCallBackView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        client_ID = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        
        
        sp_oauth = SpotifyOAuth(client_ID, client_secret, redirect_uri)
        code = request.query_params.get('code')
        token_info = sp_oauth.get_access_token(code)
        
        sp = spotipy.Spotify(auth=token_info.get('access_token'))
        user_info = sp.current_user()
        
        #Save user session to redis session (This is optional though)
        request.session[user_info['id']] = {
            user_info['id'],
            user_info['display_name'],
            token_info['access_token'],
        }
        
        #user_data = request.session.get(user_info['id']) #This was a debug line to debug something

        return Response(
            {
                'id': user_info['id'],
                'spotify_display_name': user_info['display_name'],
                'access_token': token_info['access_token'],
                'session_id': request.session[user_info['id']]
            },
            status=status.HTTP_201_CREATED)

    

class GetSessions(APIView):
    def get(self, request, format=None, *args, **kwargs):
        session_id = request.query_params.get('id')
        return Response({'session': request.session.get(session_id)})
    
class DeleteSession(APIView):
    def get(self, request, format=None, *args, **kwargs):
        session_id = request.query_params.get('id')
        check_request = request.session.get(session_id)
        try:
            del request.session[session_id]
            return Response({'message': 'done'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'message': 'Session id does not exist'})