import random


class TicTacToe:
    def __init__(self, first_player, second_player):
        self.playing_field = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        first_move = random.randint(0, 1)
        if first_move:
            print('Первым ходит', second_player)
        else:
            self.second = first_player
            print('Первым ходит', first_player)
        print('Первый игрок ходит знаком x')
        print('Второй игрок ходит знаком o')

    def whose_move(self):
        number_of_zeros = 0
        number_of_crosses = 0
        for i in self.playing_field:
            for j in i:
                if j == 'x':
                    number_of_crosses += 1
                elif j == 'o':
                    number_of_zeros += 1
        if number_of_crosses == number_of_zeros:
            return 'x'
        return 'o'

    def cross_move(self, y_coordinates, x_coordinates):
        if self.whose_move() == 'o':
            raise ValueError
        if self.playing_field[x_coordinates][y_coordinates] != '0':
            raise ValueError
        self.playing_field[x_coordinates][y_coordinates] = 'x'

    def zero_move(self, y_coordinates, x_coordinates):
        if self.whose_move() == 'x':
            raise ValueError
        if self.playing_field[x_coordinates][y_coordinates] != '0':
            raise ValueError
        self.playing_field[x_coordinates][y_coordinates] = 'o'

    def print_field(self):
        for line in self.playing_field:
            print(line)

    # def is_end_of_game(self):
    #     for


if __name__ == '__main__':
    game = TicTacToe('Алёша', 'Вася')
    print(game.whose_move())
    game.cross_move(0,2)
    game.print_field()
    # play.cross_move(0, 0)
