from django.shortcuts import get_object_or_404, render
from django.views import generic
from urllib.parse import parse_qs
from .models import League, Tier, Table, Schedule


class IndexView(generic.ListView):
    """ Implements index view via a generic list view
        and by passing the first available league by name
    """
    # Class variables
    template_name = 'league/index.html'

    def get_queryset(self):
        """Return the leagues."""
        return League.objects.order_by('-name') 


def league_view(request, league_id):
    """ Implements view

        :param request: HTTP request
        :param league_id: league identifier
    """
    tier = None
    if request.method =='POST':
        league = League.objects.create(name="My Super League", year="2020")
        league.create_tiers()
        league.create_teams()
    else:
        league = get_object_or_404(League, pk=league_id)
        tier_id = request.GET.get('tier_id')
        if tier_id:
            tier = Tier.objects.get(pk=tier_id)
    tiers = Tier.objects.order_by('-level').reverse()
    if tiers and not tier:
        tier = tiers[0]
    
    context = {'league': league, 'tier': tier}
    return render(request, 'league/league.html', context)
 

def table_view(request, league_id):
    """ Implements view

        :param request: HTTP request
        :param league_id: league identifier
    """
    league = get_object_or_404(League, pk=league_id)
    tables = Table.objects.all()
    table = None
    if request.method =='POST':
        league.create_tiers()
        league.create_teams()
        for tier in league.tier_set.all():
            tier.create_regular_season()
    else:
        table_id = request.GET.get('table_id')
        table = Table.objects.get(pk=table_id)
    if not table:
        table = tables[0]

    context = {'league': league, 'table': table}
    return render(request, 'league/table.html', context)

def match_view(request, league_id):
    """ Implements view

        :param request: HTTP request
        :param league_id: league identifier
    """
    league = get_object_or_404(League, pk=league_id)
    schedules = Schedule.objects.all()
    schedule = None
    if request.method =='POST':
        for tier in league.tier_set.all():
            tier.schedule.play_regular_season()
    else:
        schedule_id = request.GET.get('schedule_id')
        schedule = Schedule.objects.get(pk=schedule_id)
    if not schedule:
        schedule = schedules[0]

    context = {'league': league, 'schedule': schedule}
    return render(request, 'league/match.html', context)
