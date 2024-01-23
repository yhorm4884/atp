from django.contrib import admin
from .models import Player

admin.site.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']