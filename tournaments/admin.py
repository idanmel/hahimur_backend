from django.contrib import admin

from .models import Tournament, Phase

admin.site.register([
    Tournament,
    Phase,
])
