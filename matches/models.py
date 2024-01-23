from django.db import models
from players.models import Player
class Match (models.Model):
    tournament = models.CharField(max_length=255, blank=False)
    date = models.DateField()
    round = models.CharField(max_length=30)
    duration = models.FloatField()
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True,blank=True, related_name="match_winner")
    looser = models.ForeignKey(Player, on_delete=models.CASCADE, null=True,blank=True, related_name="match_looser")
    
    def __str__(self):
        return f'{self.tournament}'