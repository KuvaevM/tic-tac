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