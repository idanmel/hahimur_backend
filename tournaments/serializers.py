from rest_framework import serializers

from .models import Match, Phase, Team, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name"]


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ["id", "name"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["name", "flag"]


class MatchSerializer(serializers.ModelSerializer):
    phase = PhaseSerializer(many=False, read_only=True)
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ["id", "home_team", "away_team", "phase", "date"]
