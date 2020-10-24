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
        self.test_game.cross_move(0, 0)
        test_field = self.test_game.playing_field
        right_field = [['x', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.assertEqual(test_field, right_field)

    def test_zero_move(self):
        self.test_game.playing_field = [['x', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.test_game.zero_move(1, 0)
        test_field = self.test_game.playing_field
        right_field = [['x', '0', '0'], ['o', '0', '0'], ['0', '0', '0']]
        self.assertEqual(test_field, right_field)