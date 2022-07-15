from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from . import forms
from .models import Movie


# class MovieView(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html', context={'movie_list': movies})

class MovieView(ListView):
    # paginate_by = 2
    model = Movie
    queryset = Movie.objects.all()


# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', context={'movie': movie})

class MovieDetailView(DetailView):
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
