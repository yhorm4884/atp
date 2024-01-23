from django.db import models

class Player(models.Model):
    class typehand(models.TextChoices):
        L = 'L', 'LEFT'
        R = 'R', 'RIGHT'

    name = models.CharField(max_length=90,blank=False)
    hand = models.CharField(max_length=1, choices=typehand.choices,blank=False)
    country = models.CharField(max_length=255,blank=False)
    birthdate = models.DateField()
    
    def __str__(self):   
        return f'{self.name}'
