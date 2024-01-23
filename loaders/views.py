from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
import io
from django.http import HttpResponseForbidden

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'
    def post(self, request):
        def PlayerCreation(csv_data):
            for record in csv_data.to_dict(orient="records"):
                try:
                    if record['hand'] == "L":
                        type_hand_player = Player.typehand.L
                    else:
                        type_hand_player = Player.typehand.R
                    
                    player = Player.objects.create(
                        name = record['name'],
                        hand = type_hand_player,
                        country = record['country'],
                        birthdate = record['birthdate']
                    )
                    player.save()
                except Exception as e:
                    context['exceptions_raised'] = e
        def MatchCreation(csv_data):
            for record in csv_data.to_dict(orient="records"):
                try:
                    match = Match.objects.create(
                        tournament = record['tournament'],
                        date = record['date'],
                        round =record['round'],
                        duration =record['duration'],
                    )
                    match.save()
                except Exception as e:
                    context['exceptions_raised'] = e
        def StatsCreation(csv_data):
            for record in csv_data.to_dict(orient="records"):
                try:
                    stats = 
                except Exception as e:
                    context['exceptions_raised'] = e
        context = {
            'messages':[]
        }
        

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )
        print(type(csv.name))
        match csv.name:
            case "Player.csv":
                PlayerCreation(csv_data)
            case "Match.csv":
                MatchCreation(csv_data)
            case "Stats.csv":
                StatsCreation(csv_data)
            case _:
                return HttpResponseForbidden("Archivo insertado, no se ha reconocido.")

                
        return render(request, self.template_name, context)