from django.contrib import admin

from .models import Tournament, Phase, Team, Match

admin.site.register([
    Tournament,
    Phase,
    Team,
    Match,
])
