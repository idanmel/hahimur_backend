from django.contrib import admin

from .models import Match, Phase, Team, Tournament

admin.site.register(
    [
        Tournament,
        Phase,
        Team,
        Match,
    ]
)
