from django.urls import path
from .views import (
    ThirdPartyMovie,
    MovieColletionAPI,
    MovieListOperation
)
urlpatterns = [
    path('movies/',view = ThirdPartyMovie.as_view(),name ='third-party-movie-api'),
    path('collection/',view=MovieColletionAPI.as_view(), name='movie-collection-api'),
    path('collection/<str:uuid>/', view=MovieListOperation.as_view(), name='movie-list-operation') 
]

