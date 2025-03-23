from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

# Create your views here.


def Movie_list(request):
    movies = Movie.objects.all()
    data = {
        "movies": list(movies.values())
    }

    return JsonResponse(data)

def Movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "title": movie.title,
        "description": movie.description,
        "active": movie.active
    }
    return JsonResponse(data)
