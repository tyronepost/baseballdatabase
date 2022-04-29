import unittest

from baseballdatabase.team import Team


class TeamTest(unittest.TestCase):

    def test(self):
        team = Team('team_franchises.csv', 'batting.csv', year='1872', team_name='Troy Haymakers')

        self.assertIsNotNone(team)

        self.assertEqual(team.get_homerun_avg(), 2.50)
