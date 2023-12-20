from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('tournaments/', views.TournamentView.as_view(), name='tournaments'),
    # path('tournaments/<int:id>/matches', views.MatchesView.as_view(), name='matches'),
]