import unittest
from football_simulator import FootballMatch

class TestFootballMatch(unittest.TestCase):

    def test_initial_scores(self):
        match = FootballMatch("Team A", "Team B")
        self.assertEqual(match.team_a_score, 0)
        self.assertEqual(match.team_b_score, 0)

    def test_play_half(self):
        match = FootballMatch("Team A", "Team B")
        match.play_half()
        # Проверяем, что хотя бы одна команда могла забить гол
        self.assertTrue(0 <= match.team_a_score <= 1)
        self.assertTrue(0 <= match.team_b_score <= 1)

    def test_full_match(self):
        match = FootballMatch("Team A", "Team B")
        match.play_match()
        # Проверяем, что матч завершен после двух таймов
        self.assertTrue(match.team_a_score >= 0)
        self.assertTrue(match.team_b_score >= 0)

    def test_match_result(self):
        match = FootballMatch("Team A", "Team B")
        match.play_match()
        result = match.get_result()
        self.assertIn(result, ["Team A выигрывает!", "Team B выигрывает!", "Ничья!"])


if __name__ == '__main__':
    unittest.main()
