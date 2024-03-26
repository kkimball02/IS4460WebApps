from django.urls import path 
from .views import movieListView, movieDetailsView, addMovieView, updateMovieView, deleteMovieView
from .api_views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', movieListView, name='movie-list'),
    path('movies/<int:pk>/', movieDetailsView, name='movie-details'),
    path('add/', addMovieView, name='movie-add'),
    path('update/<int:pk>/', updateMovieView, name='movie-update'),
    path('delete/<int:pk>/', deleteMovieView, name='movie-delete'),
    path('api/movies/',MovieListCreateAPIView.as_view(), name='movie-list-create-api'),
    path('api/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-retrieve-update-destroy-api')
    
]
