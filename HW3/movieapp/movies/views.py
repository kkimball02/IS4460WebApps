from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def movieListView(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie-list.html', {'movies': movies})

def movieDetailsView(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie-details.html', {'movie': movie})

def addMovieView(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie-details', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie-add.html', {'form': form})
        
def updateMovieView(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.Post, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie-details', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie-update.html', {'form': form})

def deleteMovieView(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie-list')
    return render(request, 'movies/movie-delete.html', {'movie': movie})


        
        

