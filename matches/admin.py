from django.contrib import admin
from .models import Match
admin.site.register(Match)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['match_id', 'date']