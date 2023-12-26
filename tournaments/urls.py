from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("tournaments/", views.TournamentView.as_view(), name="tournaments"),
    path(
        "tournaments/<int:tournament_id>/matches",
        views.MatchesView.as_view(),
        name="matches",
    ),
    path("tournaments/login", views.LoginView.as_view(), name="login"),
]
