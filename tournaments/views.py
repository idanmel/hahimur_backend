from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TournamentSerializer
from .models import Tournament


class TournamentView(APIView):
    def get(self, request, format=None):
        ts = Tournament.objects.all()
        serializer = TournamentSerializer(ts, many=True)
        return Response({"data": serializer.data})