from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from . import forms
from .models import Movie, Category, Actors, Genre


class GenreYear():
    '''Жанры и года выхода фильмов'''

    def get_genre(self):
        return Genre.objects.all()

    def get_year(self):
        return Movie.objects.filter(draft=False).values('year')


class FilterMovieYear(ListView, GenreYear):
    def get_queryset(self):
        queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist('year'))|
                                        Q(genres__in=self.request.GET.getlist('genre')))
        return queryset


# class MovieView(View):      #переписан в следующем классе
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html', context={'movie_list': movies})

class MovieView(ListView, GenreYear):
    # paginate_by = 2                           # отображать 2 фильма
    model = Movie
    queryset = Movie.objects.all()


# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', context={'movie': movie})

class MovieDetailView(DetailView, GenreYear):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    success_url = '/'

    def post(self, request, pk):
        form = forms.ReviewsForms(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class Actor(DetailView, GenreYear):
    model = Actors
    template_name = 'movies/actor.html'
    slug_field = 'name'
