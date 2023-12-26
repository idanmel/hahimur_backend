import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Match, Token, Tournament
from .serializers import MatchSerializer, TournamentSerializer


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
        request_token = json.loads(request.body).get("token")
        if not request_token:
            return JsonResponse({"error": "Missing token field"}, status=422)

        try:
            user = Token.objects.get(token=request_token).friend
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Invalid token"}, status=403)

        return JsonResponse({})
