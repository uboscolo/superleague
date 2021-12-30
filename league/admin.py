from django.contrib import admin
from .models import League, Tier, Team, Venue
from .models import Schedule, Table, TableEntry, Match, Day

# Register your models here.
admin.site.register(League)
admin.site.register(Tier)
admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Table)
admin.site.register(TableEntry)
admin.site.register(Match)
admin.site.register(Day)
admin.site.register(Schedule)

