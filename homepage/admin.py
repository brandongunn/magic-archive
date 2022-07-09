from django.contrib import admin
from .models import Season2Game, Season1Game,players,commanders,comPlayed
# admin@test.com admin gunn

# Register your models here.
admin.site.register(Season2Game)
admin.site.register(Season1Game)
admin.site.register(players)
admin.site.register(commanders)
admin.site.register(comPlayed)