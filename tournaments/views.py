from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TournamentSerializer, MatchSerializer
from .models import Tournament, Match

import json


class HttpUnprocessableEntity(HttpResponse):
    status_code = 422


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

class LoginView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request):
        j = json.loads(request.body)
        if not j.get("token"):
            return HttpUnprocessableEntity("Missing Token field")
        return HttpResponse(j["token"])
