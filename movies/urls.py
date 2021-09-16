from django.urls import path
from .views import AddReview, MovieView, MovieDetailView, ActorView, FilterMoviesView

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
]