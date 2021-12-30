import random
from django.db import models

# Create your models here.


class League(models.Model):
    """ Implements a League object """

    # Class variables
    name = models.CharField(max_length=128)
    year = models.CharField(max_length=4)

    def __str__(self):
        """ __str__ overwrite """
        return self.name

    @property
    def sorted_tier_set(self):
        """ returns a list of tier in a descending order by level"""
        return self.tier_set.order_by('level')

    def create_teams(self):
        """ create teams """
        teams = {"FC Bayern München": {"Strength": 133.0, "Home field": "Allianz Arena"},
                 "Manchester City FC": {"Strength": 124.0, "Home field": "Etihad Stadium"},
                 "Liverpool FC": {"Strength": 122.0, "Home field": "Anfield"},
                 "Chelsea FC": {"Strength": 116.0, "Home field": "Stamford Bridge"},
                 "Real Madrid CF": {"Strength": 113.0, "Home field": "Santiago Bernabéu Stadium"},
                 "Paris Saint-Germain": {"Strength": 110.0, "Home field": "Le Parc des Princes"},
                 "FC Barcelona": {"Strength": 108.0, "Home field": "Camp Nou"},
                 "Juventus": {"Strength": 106.0, "Home field": "Allianz Stadium"},
                 "Manchester United": {"Strength": 104.0, "Home field": "Old Trafford"},
                 "Club Atlético de Madrid": {"Strength": 100.0, "Home field": "Wanda Metropolitano Stadium"},
                 "Sevilla FC": {"Strength": 88.0, "Home field": "Ramon Sanchez-Pizjuan Stadium"},
                 "AS Roma": {"Strength": 86.0, "Home field": "Stadio Olimpico"},
                 "Tottenham Hotspur": {"Strength": 83.0, "Home field": "Tottenham Hotspur Stadium"},
                 "AFC Ajax": {"Strength": 81.5, "Home field": "Johan Cruyff Arena"},
                 "Arsenal FC": {"Strength": 80.0, "Home field": "Emirates Stadium"},
                 "Borussia Dortmund": {"Strength": 78.0, "Home field": "Signal Iduna Park"},
                 "FC Porto": {"Strength": 78.0, "Home field": "Estádio do Dragão"},
                 "RB Leipzig": {"Strength": 75.0, "Home field": "Red Bull Arena Leipzig"},
                 "FC Shakhtar Donetsk": {"Strength": 71.0, "Home field": "National Sports Complex Olympiyskiy"},
                 "Villarreal CF": {"Strength": 70.0, "Home field": "Estadio de la Cerámica"},
                 "FC Salzburg": {"Strength": 70.0, "Home field": "Red Bull Arena Salzburg"},
                 "Olympique Lyonnais": {"Strength": 66.0, "Home field": "Groupama Stadium"},
                 "FC Internazionale Milano": {"Strength": 65.0, "Home field": "San Siro Stadium"},
                 "SSC Napoli": {"Strength": 64.0, "Home field": "Diego Armando Maradona Stadium"},
                 "Atalanta BC": {"Strength": 59.5, "Home field": "Gewiss Stadium"},
                 "SL Benfica": {"Strength": 56.0, "Home field": "Estádio do Sport Lisboa e Benfica"},
                 "Sporting Clube de Portugal": {"Strength": 54.5, "Home field": "José Alvalade Stadium"},
                 "FC Basel 1893": {"Strength": 53.0, "Home field": "St. Jakob-Park"},
                 "SS Lazio": {"Strength": 51.0, "Home field": "Stadio Olimpico"},
                 "Bayer 04 Leverkusen": {"Strength": 49.0, "Home field": "BayArena"},
                 "SK Slavia Praha": {"Strength": 48.0, "Home field": "Sinobo Stadium"},
                 "GNK Dinamo Zagreb": {"Strength": 47.5, "Home field": "Stadion Maksimir"},
                 "FC Zenit": {"Strength": 46.0, "Home field": "Gazprom Arena"},
                 "FC Dynamo Kyiv": {"Strength": 44.0, "Home field": "National Sports Complex Olympiyskiy"},
                 "Eintracht Frankfurt": {"Strength": 43.0, "Home field": "Deutsche Bank Park"},
                 "FK Crvena zvezda": {"Strength": 40.0, "Home field": "Rajko Mitic Stadium"},
                 "Valencia CF": {"Strength": 40.0, "Home field": "Mestalla Stadium"},
                 "Olympiacos FC": {"Strength": 39.0, "Home field": "Karaiskaki Stadium"},
                 "Club Brugge": {"Strength": 38.5, "Home field": "Jan Breydel Stadium"},
                 "AC Milan": {"Strength": 38.0, "Home field": "San Siro Stadium"},
                 "F.C. Copenhagen": {"Strength": 37.5, "Home field": "Parken"},
                 "Rangers FC": {"Strength": 37.25, "Home field": "Ibrox Stadium"},
                 "BSC Young Boys": {"Strength": 37.0, "Home field": "Wankdorf Stadium"},
                 "SC Braga": {"Strength": 37.0, "Home field": "Estádio Municipal de Braga"},
                 "Olympique de Marseille": {"Strength": 34.0, "Home field": "Orange Vélodrome"},
                 "Celtic FC": {"Strength": 33.0, "Home field": "Celtic Park"},
                 "Beşiktaş JK": {"Strength": 33.0, "Home field": "Vodafone Park"},
                 "FC Lokomotiv Moskva": {"Strength": 33.0, "Home field": "RZD Arena"},
                 "PFC CSKA Moskva": {"Strength": 33.0, "Home field": "VEB Arena"},
                 "LASK": {"Strength": 32.0, "Home field": "Linzer Stadion"},
                 "FC Viktoria Plzeň": {"Strength": 31.0, "Home field": "Doosan Arena"},
                 "LOSC Lille": {"Strength": 30.0, "Home field": "Stade Pierre Mauroy"},
                 "PSV Eindhoven": {"Strength": 29.0, "Home field": "Philips Stadion"},
                 "Galatasaray AŞ": {"Strength": 27.0, "Home field": "Nef Stadyumu"},
                 "Stade Rennais FC": {"Strength": 27.0, "Home field": "Roazhon Park"},
                 "FC Krasnodar": {"Strength": 26.5, "Home field": "Krasnodar Stadium"},
                 "Feyenoord": {"Strength": 26.0, "Home field": "Feyenoord Stadium"},
                 "AZ Alkmaar": {"Strength": 25.5, "Home field": "AFAS stadium"},
                 "KAA Gent": {"Strength": 25.5, "Home field": "KAA Gent Stadium"},
                 "FC Spartak Moskva": {"Strength": 25.5, "Home field": "Otkrytie Bank Arena"},
                 "İstanbul Başakşehir": {"Strength": 25.0, "Home field": "Başakşehir Fatih Terim Stadium"},
                 "Qarabağ FK": {"Strength": 24.0, "Home field": "Azərsun Arena"},
                 "Real Sociedad de Fútbol": {"Strength": 24.0, "Home field": "Reale Arena"},
                 "Maccabi Tel-Aviv FC": {"Strength": 23.5, "Home field": "Bloomfield Stadium"},
                 "FK Partizan": {"Strength": 23.5, "Home field": "Partizan Stadium"},
                 "Malmö FF": {"Strength": 23.5, "Home field": "Eleda Stadium"},
                 "TSG 1899 Hoffenheim": {"Strength": 23.0, "Home field": "Rhein-Neckar-Arena"},
                 "FC Sheriff Tiraspol": {"Strength": 22.5, "Home field": "Sheriff Sports Complex"},
                 "VfL Wolfsburg": {"Strength": 22.5, "Home field": "Volkswagen Arena"},
                 "PFC Ludogorets 1945": {"Strength": 22.0, "Home field": "Huvepharma Arena"},
                 "AS Monaco FC": {"Strength": 21.0, "Home field": "Stade Louis II"},
                 "VfL Borussia Mönchengladbach": {"Strength": 21.0, "Home field": "Borussia-Park"},
                 "FC Astana": {"Strength": 20.5, "Home field": "Astana Arena"},
                 "PAOK FC": {"Strength": 20.0, "Home field": "Toumba Stadium"},
                 "AEK Athens FC": {"Strength": 20.0, "Home field": "Main Olympic Stadium"},
                 "West Ham United FC": {"Strength": 19.842, "Home field": "London Stadium"},
                 "Leicester City FC": {"Strength": 19.842, "Home field": "King Power Stadium"},
                 "Wolverhampton Wanderers FC": {"Strength": 19.842, "Home field": "Molineux Stadium"},
                 "Burnley FC": {"Strength": 19.842, "Home field": "Turf Moor"},
                 "Everton FC": {"Strength": 19.842, "Home field": "Goodison Park"}}
        num_teams = len(teams)
        tiers = ["Champions", "Challengers", "Contenders", "Dreamers"]
        num_tiers = len(tiers)
        team_ratio = num_teams // num_tiers
        for idx, (team_name, team_properties) in enumerate(teams.items()):
            tier_name = tiers[idx // team_ratio]
            try:
                tier = self.tier_set.get(name=tier_name)
            except Tier.DoesNotExist:
                tier = Tier.objects.create(name=tier_name, league=self, level=idx+1)
            strength = team_properties.get('Strength')
            venue_name = team_properties.get('Home field')
            try:
                venue = Venue.objects.get(name=venue_name)
            except Venue.DoesNotExist:
                venue = Venue.objects.create(name=venue_name)
            try:
                team = Team.objects.get(name=team_name)
            except Team.DoesNotExist:
                Team.objects.create(name=team_name, strength=strength, tier=tier, field=venue)
            else:
                if team.tier != tier or team.strength != strength or team.field != venue:
                    team.delete()
                    Team.objects.create(name=team_name, strength=strength, tier=tier, field=venue)
         
    def create_tiers(self):
        """ create tiers """
        tiers = ["Champions", "Challengers", "Contenders", "Dreamers"]
        for level, tier_name in enumerate(tiers):
            set_level = level + 1
            try:
                tier = self.tier_set.get(name=tier_name)
            except Tier.DoesNotExist:
                Tier.objects.create(name=tier_name, league=self, level=set_level)
            else:
                if tier.level != set_level:
                    tier.delete()
                    Tier.objects.create(name=tier_name, league=self, level=set_level)


class Tier(models.Model):
    """ Implements a Tier object """

    # Class variables
    name = models.CharField(max_length=128)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    level = models.IntegerField() 
    playoff_series = models.IntegerField(default=0) 
    relegations = models.IntegerField(default=4) 

    def __str__(self):
        """ __str__ overwrite """
        return self.name

    @property
    def table(self):
        """ returns the Table """
        try:
            table = self.table_set.get(name=self.name)
        except Table.DoesNotExist:
            table = None
        return table

    @property
    def schedule(self):
        """ returns the Schedule """
        try:
            schedule = self.schedule_set.get(year=self.league.year)
        except Schedule.DoesNotExist:
            schedule = None
        return schedule

    def create_table(self):
        """ creates the Table """
        if self.table:
            self.table.delete()
        table = Table.objects.create(name=self.name, year=self.league.year, tier=self)
        return table

    def create_schedule(self):
        """ returns the Table """
        if self.schedule:
            self.schedule.delete()
        schedule = Schedule.objects.create(year=self.league.year, tier=self, current_day=1)
        return schedule

    def create_regular_season(self):
        """ create the regular season """
        schedule = self.create_schedule()
        schedule.create_regular_season()
        table = self.create_table()
        table.populate(teams=self.team_set.all())


class Table(models.Model):
    """ Implements a Table object """

    # Class variables
    name = models.CharField(max_length=128)
    year = models.CharField(max_length=4)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        """ __str__ overwrite """
        return self.name

    @property
    def sorted_tableentry_set(self):
        """ returns a list of tier in a descending order by level"""
        return self.tableentry_set.order_by('points').reverse()

    def populate(self, teams):
        """ Populates the table
       
           :param teams: list of Teams
        """
        for team in teams:
            try:
                entry = self.tableentry_set.get(team_name=team.name)
            except TableEntry.DoesNotExist:
                entry = TableEntry.objects.create(team_name=team.name, table=self)
            else:
                entry.delete()
                entry = TableEntry.objects.create(team_name=team.name, table=self)


class TableEntry(models.Model):
    """ Implements a TableEntry object """

    # Class variables
    team_name = models.CharField(max_length=128)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    points = models.IntegerField(default=0) 
    played = models.IntegerField(default=0) 
    wins = models.IntegerField(default=0) 
    losses = models.IntegerField(default=0) 
    draws = models.IntegerField(default=0) 
    goals_for = models.IntegerField(default=0) 
    goals_against = models.IntegerField(default=0) 

    class Meta:
        """ Meta class """
        verbose_name_plural = "Table entries"

    def __str__(self):
        """ __str__ overwrite """
        return self.team_name
       

class Venue(models.Model):
    """ Implements a Venue object """

    # Class variables
    name = models.CharField(max_length=128)

    def __str__(self):
        """ __str__ overwrite """
        return self.name


class Team(models.Model):
    """ Implements a Team object """

    # Class variables
    name = models.CharField(max_length=128)
    strength = models.DecimalField(max_digits=7, decimal_places=4)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)
    field = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        """ __str__ overwrite """
        return self.name


class Schedule(models.Model):
    """ Implements a Schedule object """

    # Class variables
    year = models.CharField(max_length=4)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    current_day = models.IntegerField(default=0)
 
    def __str__(self):
        """ __str__ overwrite """
        return f"{self.tier.name} - {self.year}"

    @property
    def sorted_day_set(self):
        """ returns in order days """
        return self.day_set.order_by('number')

    @property
    def day(self):
        """ returns current day """
        return self.day_set.get(number=self.current_day)

    def create_regular_season(self):
        """ creates a regular season schedule """
        team_list = self.tier.team_set.all()
        rotating_table = {idx+1: team for idx, team in enumerate(team_list)}
        num = 0
        num_teams = len(team_list)
        num_days = num_teams - 1
        num_matches = num_teams // 2
        while num < num_days:
            num += 1
            new_day_1st_half = Day.objects.create(number=num, schedule=self)
            new_day_2nd_half = Day.objects.create(number=num+num_days, schedule=self)
            match_num = 0
            while match_num < num_matches:
                match_num += 1
                if match_num == 1:
                    team1 = rotating_table[match_num]
                    team2 = rotating_table[match_num + 1]
                else:
                    team1 = rotating_table[match_num + 1]
                    team2 = rotating_table[num_teams - match_num + 2]
                if num % 2:
                    tmp_team = team2
                    team2 = team1
                    team1 = tmp_team
                new_match_1st_half = Match.objects.create(day=new_day_1st_half, team1=team1, team2=team2, venue=team1.field)
                new_match_2nd_half = Match.objects.create(day=new_day_2nd_half, team1=team2, team2=team1, venue=team2.field)
            curr_val = 0
            for entry, team in rotating_table.items():
                if entry == 2:
                    curr_val = team
                    rotating_table[entry] = rotating_table[num_teams]
                elif entry > 2:
                    stored_val = team
                    rotating_table[entry] = curr_val
                    curr_val = stored_val

    def play_regular_season(self):
        """ play regular season schedule """
        num_days = len(self.day_set.all())
        if self.current_day <= num_days:
            for match in self.day.match_set.all():
                match.play(phase="regular")
        self.current_day += 1
        self.save()

          
class Day(models.Model):
    """ Implements a Day object """

    # Class variables
    number = models.IntegerField(default=0)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        """ __str__ overwrite """
        return f"{self.schedule.tier.name} - {self.schedule.year} - Day {self.number}"


class Match(models.Model):
    """ Implements a Match object """

    # Class variables
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    time = models.CharField(max_length=64, default='1:00 PM')
    result = models.CharField(max_length=8, default='0-0')
    home_factor = models.DecimalField(max_digits=2, decimal_places=1, default=2.0)
    luck_factor = models.DecimalField(max_digits=2, decimal_places=1, default=8.0)

    class Meta:
        """ Meta class """
        verbose_name_plural = "Matches"

    @property
    def home_team(self):
        """ returns home team """
        return self.team1 if self.team1.field == self.venue else None  

    @property
    def away_team(self):
        """ returns away team """
        return self.team2 if self.team1.field == self.venue else None  

    def __str__(self):
        """ __str__ overwrite """
        team_str = f"{self.team1.name}-{self.team2.name}"
        return f"Day {self.day.number}: {team_str}"

    @staticmethod
    def generate_score(result, phase="regular"):
        """ generates score """
        regular_home_table = {'1-0': 0.125, '2-0': 0.090, '2-1': 0.093, '3-0': 0.045,
                              '4-0': 0.025, '3-1': 0.045, '3-2': 0.020, '4-1': 0.015,
                              '5-0': 0.005, '4-2': 0.007, '5-1': 0.005, '6-0': 0.002,
                              '4-3': 0.003, '5-2': 0.001, '6-1': 0.001, '7-0': 0.001}
        regular_away_table = {'0-1': 0.065, '0-2': 0.050, '1-2': 0.053, '0-3': 0.015,
                              '0-4': 0.015, '1-3': 0.025, '2-3': 0.015, '1-4': 0.010,
                              '0-5': 0.003, '2-4': 0.002, '1-5': 0.002, '0-6': 0.001,
                              '3-4': 0.002, '2-5': 0.001, '1-6': 0.001, '0-7': 0.001}
        regular_draw_table = {'0-0': 0.085, '1-1': 0.120, '2-2': 0.045, '3-3': 0.007}

        extra_home_table = {'1-0': 0.150, '2-0': 0.115, '2-1': 0.110, '3-0': 0.070}
        extra_away_table = {'0-1': 0.095, '0-2': 0.075, '1-2': 0.080, '0-3': 0.040}
        extra_draw_table = {'0-0': 0.120, '1-1': 0.145}

        score_tables = {('regular', 0): regular_draw_table,
                        ('regular', 1): regular_home_table,
                        ('regular', 2): regular_away_table,
                        ('extra', 0): extra_draw_table,
                        ('extra', 1): extra_home_table,
                        ('extra', 2): extra_away_table}

        score_table = score_tables.get((phase, result))
        total = sum(score_table.values())
        roll = random.uniform(0, total)

        current_val = 0
        score = '0-0'
        for res, prob in score_table.items():
            current_val += prob
            if roll <= current_val:
                score = res
                break
        return score

    def play(self, phase="regular"):
        """ finalizes match """
        # 1) Strengths
        strength1 = float(self.team1.strength)
        strength2 = float(self.team2.strength)
        # 2) Home advantage
        if self.team1 == self.home_team:
            strength1 *= float(self.home_factor)
        # 3) Luck factor
        luck1 = random.uniform(1.0, float(self.luck_factor))
        strength1 *= luck1
        luck2 = random.uniform(1.0, float(self.luck_factor))
        strength2 *= luck2
        strength_ratio = strength1 / strength2
        entry1 = TableEntry.objects.get(team_name=self.team1.name)
        entry2 = TableEntry.objects.get(team_name=self.team2.name)
        entry1.played += 1
        entry2.played += 1
        if strength_ratio > 2:
            entry1.points += 3
            entry1.wins += 1
            entry2.losses += 1
            score = self.generate_score(result=1, phase=phase)
        elif strength_ratio < 0.5:
            entry2.points += 3
            entry2.wins += 1
            entry1.losses += 1
            score = self.generate_score(result=2, phase=phase)
        else:
            entry1.points += 1
            entry2.points += 1
            entry1.draws += 1
            entry2.draws += 1
            score = self.generate_score(result=0, phase=phase)
        self.result = score
        score_fields = score.split('-') 
        entry1.goals_for += int(score_fields[0])
        entry1.goals_against += int(score_fields[1])
        entry2.goals_for += int(score_fields[1])
        entry2.goals_against += int(score_fields[0])
        entry1.save()
        entry2.save()
        self.save()
 
