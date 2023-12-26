from django.contrib import admin

from .models import Match, Phase, Prediction, Team, Token, Tournament

admin.site.register(
    [
        Tournament,
        Phase,
        Team,
        Match,
        Token,
        Prediction,
    ]
)
