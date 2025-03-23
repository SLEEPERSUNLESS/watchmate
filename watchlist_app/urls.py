from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.Movie_list, name="movie-list"),
    path("<int:pk>", views.Movie_details, name="movie-details")
]
