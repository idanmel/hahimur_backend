from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TournamentSerializer, MatchSerializer
from .models import Tournament, Match


class TournamentView(APIView):
    def get(self, request, format=None):
        ts = Tournament.objects.all()
        serializer = TournamentSerializer(ts, many=True)
        return Response({"data": serializer.data})
    

class MatchesView(APIView):
    def get(self, request, tournament_id, format=None):
        matches = Match.objects.filter(phase__tournament_id=tournament_id)
        serializer = MatchSerializer(matches, many=True)
        return Response({"data": serializer.data})
