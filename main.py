from piece import Piece
import sys

class Game:
    top = 'red'
    bottom = 'black'
    # teams = ['black', 'red']
    piece = ['chariot', 'horse', 'elephant', 'advisor', 'general', 'soldier', 'canon']
    # chess_pcs_dist = {'soldier': 5, 'cannon': 2, 'chariot': 2, 'horse': 2, 'elephant': 2, 'advisor': 2, 'general': 1}
    black_pieces = {}
    red_pieces = {}
    board = []

    def __init__(self):
        if self.top == 'red':
            j = 1
            for i in range(0, 9, 2):
                self.red_pieces['soldier_' + str(j)] = Piece('red_soldier_' + str(j), 'red', 'soldier', (3, i))
                self.black_pieces['soldier_' + str(j)] = Piece('black_soldier_' + str(j), 'black', 'soldier', (6, i))
                j += 1

            j = 1
            for i in range(0, 4):
                self.red_pieces[self.piece[i] + '_' + str(j)] = Piece('red_' + self.piece[i] + '_' + str(j), 'red',
                                                                      self.piece[i], (0, i))
                self.black_pieces[self.piece[i] + '_' + str(j)] = Piece('black_' + self.piece[i] + '_' + str(j),
                                                                        'black', self.piece[i], (9, i))
                j += 1
                self.red_pieces[self.piece[i] + '_' + str(j)] = Piece('red_' + self.piece[i] + '_' + str(j), 'red',
                                                                      self.piece[i], (0, 8-i))
                self.black_pieces[self.piece[i] + '_' + str(j)] = Piece('black_' + self.piece[i] + '_' + str(j),
                                                                        'black', self.piece[i], (9, 8-i))
                # self.init_map['red_' + self.piece[i] + '_' + str(j)] = (0, 8 -i)
                # self.init_map['black_' + self.piece[i] + '_' + str(j)] = (9, 8 - i)

            #self.init_map['red_' + self.piece[5]] = (0, 5)
            #self.init_map['black_' + self.piece[5]] = (9, 5)
            self.red_pieces['general'] = Piece('red_general', 'red', 'general', (0, 4))
            self.black_pieces['general'] = Piece('black_general', 'black', 'general', (9, 4))

            j = 1
            self.red_pieces['cannon_' + str(j)] = Piece('red_cannon_' + str(j), 'red', 'cannon', (2, 1))
            self.black_pieces['cannon_' + str(j)] = Piece('black_cannon_' + str(j), 'black', 'cannon', (7, 1))

            j += 1
            self.red_pieces['cannon_' + str(j)] = Piece('red_cannon_' + str(j), 'red', 'cannon', (2, 7))
            self.black_pieces['cannon_' + str(j)] = Piece('black_cannon_' + str(j), 'black', 'cannon', (7, 7))

        else:
            j = 1
            for i in range(0, 9, 2):
                self.red_pieces['soldier_' + str(j)] = Piece('red_soldier' + str(j), 'red', 'soldier', (6, i))
                self.black_pieces['soldier_' + str(j)] = Piece('black_soldier' + str(j), 'black', 'soldier', (3, i))
                j += 1

            j = 1
            for i in range(0, 4):
                self.red_pieces[self.piece[i] + '_' + str(j)] = Piece('red_' + self.piece[i] + +'_' + str(j), 'red',
                                                                      self.piece[i], (9, i))
                self.black_pieces[self.piece[i] + '_' + str(j)] = Piece('black_' + self.piece[i] + +'_' + str(j),
                                                                        'black', self.piece[i], (0, i))
                j += 1
                self.red_pieces[self.piece[i] + '_' + str(j)] = Piece('red_' + self.piece[i] + +'_' + str(j), 'red',
                                                                      self.piece[i], (9, 8 - i))
                self.black_pieces[self.piece[i] + '_' + str(j)] = Piece('black_' + self.piece[i] + +'_' + str(j),
                                                                        'black', self.piece[i], (0, 8 - i))
                # self.init_map['red_' + self.piece[i] + '_' + str(j)] = (0, 8 -i)
                # self.init_map['black_' + self.piece[i] + '_' + str(j)] = (9, 8 - i)

            # self.init_map['red_' + self.piece[5]] = (0, 5)
            # self.init_map['black_' + self.piece[5]] = (9, 5)
            self.red_pieces['general'] = Piece('red_general', 'red', 'general', (9, 4))
            self.black_pieces['general'] = Piece('black_general', 'black', 'general', (0, 4))

            j = 1
            self.red_pieces['cannon_' + str(j)] = Piece('red_cannon_' + str(j), 'red', 'cannon', (7, 1))
            self.black_pieces['cannon_' + str(j)] = Piece('black_cannon_' + str(j), 'black', 'cannon', (2, 1))

            j += 1
            self.red_pieces['cannon_' + str(j)] = Piece('red_cannon_' + str(j), 'red', 'cannon', (7, 7))
            self.black_pieces['cannon_' + str(j)] = Piece('black_cannon_' + str(j), 'black', 'cannon', (2, 7))

        self.init_board()

    def print_pieces(self):
        for key in self.red_pieces.keys():
            x, y = self.red_pieces[key].get_current_pos()
            print(key + ": (" + str(x) + ',' + str(y) + ')')

        print("\n")
        for key in self.black_pieces.keys():
            x, y = self.black_pieces[key].get_current_pos()
            print(key + ": (" + str(x) + ',' + str(y) + ')')

    def init_board(self):
        for i in range(0, 10):
            board_y = []
            for j in range(0, 9):
                board_y.append(".")
            self.board.append(board_y)

        for key in self.red_pieces.keys():
            x, y = self.red_pieces[key].get_current_pos()
            self.board[x][y] = self.red_pieces[key]

        for key in self.black_pieces.keys():
            x, y = self.black_pieces[key].get_current_pos()
            self.board[x][y] = self.black_pieces[key]

    def print_board(self):
        for i in range(10):
            for j in range(9):
                sys.stdout.write(self.board[i][j].__str__() + " ")
            print()


if __name__ == '__main__':
    game = Game()
    game.print_pieces()
    game.print_board()