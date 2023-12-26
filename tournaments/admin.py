from django.contrib import admin

from .models import Match, Phase, Team, Token, Tournament

admin.site.register(
    [
        Tournament,
        Phase,
        Team,
        Match,
        Token,
    ]
)
