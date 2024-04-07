## Vue3 and Django Project that combines AI api, Spotify API, Vue, Django, 0Auth if necessary.

## Project Details:
1. Build the frontend of the website using web 3
2. Django (Microservices architecture style if necessary) for the backend
3. Typescript for frontend scripting
4. 0Auth for signin purposes if necessary, or Spotify API for signing in with spotify data
5. AI models for understanding songs and learning details of the song and displaying them as an api.
6. If current AI models do not exist maybe build one? else use spotify api (Should be a very secondary practice)
7. Once details of a song is gotten use spotify api to generate and recommend songs based on the details for users. 
8. Built model spits out songs (maybe up to 12) for users to add to their spotify playlist.


## Tech Stack
1. Frontend: Vue3, Typescript, scss
2. Backend: Python, Django
3. Cloud Provider: Microsoft Azure
4. Necessary APIs: Spotify Developer API, 0Auth (debatable)
5. Frontend Hosting service: Render (They've got nice free tiers though it wouldn't hurt to look at better options)
6. Database (if necessary): Mongodb (Main database), Cache (Redis)





from django.urls import path
from .views import *

urlpatterns = [
    path('spotify/login/', SpotifyLoginView.as_view(), name='spotify_login'),
    path('spotify/callback/', SpotifyCallBackView.as_view(), name='spotify_callback'),
]