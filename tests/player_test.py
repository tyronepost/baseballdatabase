import unittest
from baseballdatabase.player import Player


class PlayerTest(unittest.TestCase):
    def test_instance(self):
        player = Player(player_id='playerId', team_id='OAK', home_runs=3)
        self.assertEqual(player.player_id, 'playerId')
        self.assertEqual(player.team_id, 'OAK')
        self.assertEqual(player.home_runs, 3)

    def test_select_players_where(self):
        players = Player.select_players_where('batting.csv', team_id='TRO', year='1872')
        self.assertTrue(len(players), 2)
        self.assertTrue(isinstance(players[0], Player))
        self.assertTrue(isinstance(players[1], Player))

        self.assertEqual(players[0].player_id, 'player1')
        self.assertEqual(players[0].home_runs, 2)

        self.assertEqual(players[1].player_id, 'player4')
        self.assertEqual(players[1].home_runs, 3)


if __name__ == '__main__':
    unittest.main()