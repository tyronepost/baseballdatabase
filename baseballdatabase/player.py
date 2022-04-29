import csv
from baseballdatabase.utils import get_header_dict


class Player(object):
    TEAM_ID = 'teamID'
    PLAYER_ID = 'playerID'
    HOME_RUNS = 'HR'
    YEAR_ID = 'yearID'

    def __init__(self, player_id=None, team_id=None, home_runs=None):
        self.player_id = player_id
        self.team_id = team_id
        self.home_runs = int(home_runs)

    @staticmethod
    def select_players_where(file_path, team_id=None, year=None):
        ret = []
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            header_dict = get_header_dict(data.pop(0))

            for row in data:
                if row[header_dict[Player.TEAM_ID]] == team_id and row[header_dict[Player.YEAR_ID]] == year:
                    ret.append(Player(team_id=team_id,
                                      player_id=row[header_dict[Player.PLAYER_ID]],
                                      home_runs=row[header_dict[Player.HOME_RUNS]]))

        return ret
