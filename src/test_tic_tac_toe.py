import unittest
from src.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.test_game = TicTacToe('Алёша', 'Вася')

    def test_whose_move(self):
        self.test_game.playing_field = [['x', 'o', '0'], ['x', 'o', '0'], ['0', '0', '0']]
        test_move = self.test_game.whose_move()
        right_move = 'x'
        self.assertEqual(test_move, right_move)
        self.test_game.playing_field = [['x', 'o', '0'], ['x', 'o', '0'], ['0', 'x', '0']]
        test_move = self.test_game.whose_move()
        right_move = 'o'
        self.assertEqual(test_move, right_move)

    def test_cross_move(self):
        self.test_game.cross_move(0, 1)
        test_field = self.test_game.playing_field
        right_field = [['0', '0', '0'], ['x', '0', '0'], ['0', '0', '0']]
        self.assertEqual(test_field, right_field)

    def test_zero_move(self):
        self.test_game.playing_field = [['x', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.test_game.zero_move(1, 0)
        test_field = self.test_game.playing_field
        right_field = [['x', 'o', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.assertEqual(test_field, right_field)

    def test_who_is_win(self):
        self.test_game.playing_field = [['x', 'x', 'x'], ['0', '0', '0'], ['0', '0', '0']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'x'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['x', 'o', 'x'], ['0', 'x', '0'], ['0', '0', 'x']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'x'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['x', '0', 'x'], ['x', '0', '0'], ['x', '0', '0']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'x'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['o', 'o', 'o'], ['0', '0', '0'], ['0', '0', '0']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'o'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['o', 'x', 'x'], ['0', 'o', '0'], ['0', '0', 'o']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'o'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['o', '0', 'x'], ['o', '0', '0'], ['o', '0', '0']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'o'
        self.assertEqual(right_winner, test_winner)
        self.test_game.playing_field = [['o', '0', 'x'], ['x', '0', '0'], ['o', '0', '0']]
        test_winner = self.test_game.who_is_win()
        right_winner = 'tie'
        self.assertEqual(right_winner, test_winner)


