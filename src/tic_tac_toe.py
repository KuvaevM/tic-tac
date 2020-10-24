import random


class TicTacToe:
    def __init__(self, first_player, second_player):
        """Заводит новое игровое поле. Определяет, какой из двух игроков будет ходить первым. Печатает необходимую
        информацию """
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
        """Возвращает, кто сейчас ходит, крестик или нолик"""
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
        """Записывает в поле с заданными координатами крестик. Если поле не пусто или сейчас не тот ход возбуждает
        ValueError """
        if self.whose_move() == 'o':
            raise ValueError
        if self.playing_field[x_coordinates][y_coordinates] != '0':
            raise ValueError
        self.playing_field[x_coordinates][y_coordinates] = 'x'

    def zero_move(self, y_coordinates, x_coordinates):
        """Записывает в поле с заданными координатами нолик. Если поле не пусто или сейчас не тот ход возбуждает
        ValueError"""
        if self.whose_move() == 'x':
            raise ValueError
        if self.playing_field[x_coordinates][y_coordinates] != '0':
            raise ValueError
        self.playing_field[x_coordinates][y_coordinates] = 'o'

    def print_field(self):
        """Печатает игровое поле"""
        for line in self.playing_field:
            print(line)

    def who_is_win(self):
        """Определяет, кто победил. Если крестик - возвращает x, если нолик - o, а если ничья - tie"""
        columns_and_diagonals = [[], [], [], [], [], []]
        number_of_line = 0
        for line in self.playing_field:
            if line == ['o', 'o', 'o']:
                return 'o'
            if line == ['x', 'x', 'x']:
                return 'x'
            for number_of_column in range(3):
                columns_and_diagonals[number_of_column].append(line[number_of_column])
            columns_and_diagonals[3].append(line[number_of_line])
            columns_and_diagonals[4].append(line[2 - number_of_line])
            number_of_line += 1
        for combination in columns_and_diagonals:
            if combination == ['o', 'o', 'o']:
                return 'o'
            if combination == ['x', 'x', 'x']:
                return 'x'
        return 'tie'

    def is_end_of_game(self):
        """Определяет, закончилась ли игра"""
        if self.who_is_win() == 'x' or self.who_is_win() == 'o':
            return True
        for line in self.playing_field:
            if '0' in line:
                return False
        return True


if __name__ == '__main__':
    game = TicTacToe('Алёша', 'Вася')
    print(game.whose_move())
    game.cross_move(0, 2)
    game.print_field()

