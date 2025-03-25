from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", views.WatchDetailAV.as_view(), name="movie-details"),
    path("stream/", views.StreamPlatformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>", views.StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    
    # path("review/", views.ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", views.ReviewDetail.as_view(), name="review-detail"),
    
    path("stream/<int:pk>/review-create", views.ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review", views.ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>", views.ReviewDetail.as_view(), name="review-detail"),
    
]
