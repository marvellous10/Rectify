from django.urls import path
from .views import *

urlpatterns = [
    path('post/', SendFeedback.as_view(), name='send-feedback'),
]
