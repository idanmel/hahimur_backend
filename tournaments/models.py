from django.conf import settings
from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Phase(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tournament} - {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Match(models.Model):
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="home_team"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="away_team"
    )
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    date = models.DateTimeField()
    ordering = ["date"]

    def __str__(self):
        return f"{self.phase}: {self.home_team} - {self.away_team}"

    class Meta:
        verbose_name_plural = "Matches"


class Token(models.Model):
    token = models.CharField(max_length=200)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.friend}: {self.token}"


class Prediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)

    def __str__(self):
        return (
            f"{self.friend}, {self.match.phase}, "
            f"Home: {self.match.home_team} {self.home_goals} - Away: {self.match.away_team} {self.away_goals}. "
        )
