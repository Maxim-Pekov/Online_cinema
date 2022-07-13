from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Movie


# class MovieView(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movies.html', context={'movie_list': movies})

class MovieView(ListView):
    # paginate_by = 2
    model = Movie
    template_name = 'movies/movies.html'
    queryset = Movie.objects.all()


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', context={'movie': movie})