
import csv

from baseballdatabase.player import Player
from baseballdatabase.utils import get_header_dict


class Team(object):
    FRANCHISE_ID = 'franchID'
    FRANCHISE_NAME = 'franchName'

    def __init__(self, team_franchises_file, player_file, year=None, team_name=None):
        self.year = year
        self.team_name = team_name
        self.team_id = Team.get_team_id(team_franchises_file, team_name)
        self.players = Player.select_players_where(player_file, year=year, team_id=self.team_id)

    def get_homerun_avg(self):
        total_homeruns = 0

        for player in self.players:
            total_homeruns += player.home_runs

        return round(total_homeruns / len(self.players), 2)

    @staticmethod
    def get_team_id(team_franchise_file, team_name):
        with open(team_franchise_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            header_dict = get_header_dict(data.pop(0))

            for row in data:
                if row[header_dict[Team.FRANCHISE_NAME]] == team_name:
                    return row[header_dict[Team.FRANCHISE_ID]]

        raise RuntimeError(f'Cannot find team: {team_name}')
