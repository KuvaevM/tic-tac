import random


class TicTacToe:
    def __init__(self, first_player, second_player):
        self.playing_field = [['0', '0', '0'], ['0', 'x', '0'], ['0', '0', '0']]
        first_move = random.randint(0, 1)
        if first_move:
            print('Первым ходит', second_player)
        else:
            print('Первым ходит', first_player)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play = TicTacToe('x', 'o')
    # play.cross_move(0, 0)
