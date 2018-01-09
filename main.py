from piece import Piece
from utility import tuple_to_str
import sys


class Game:
    top = 'red'
    bottom = 'black'
    teams = ['black', 'red']
    piece = ['chariot', 'horse', 'elephant', 'advisor', 'general', 'soldier', 'cannon']
    chess_pcs_dist = {'soldier': 5, 'cannon': 2, 'chariot': 2, 'horse': 2, 'elephant': 2, 'advisor': 2, 'general': 1}
    black_pieces = {}
    red_pieces = {}
    board = []
    top_init_pos = {}
    bottom_init_pos = {}
    BOARD_IS_EMPTY = "   .   "

    def __init__(self):
        self.init_team()
        self.init_dict()
        self.generate_init_pos()
        self.init_piece_pos()
        self.init_board()

    def init_team(self):
        self.top = 'red'
        self.bottom = 'black'

    def init_dict(self):
        for piece in self.piece:
            for i in range(self.chess_pcs_dist[piece]):
                self.black_pieces[piece + '_' + str(i)] = Piece('black_' + piece + '_' + str(i), 'black', piece)

        for piece in self.piece:
            for i in range(self.chess_pcs_dist[piece]):
                self.red_pieces[piece + '_' + str(i)] = Piece('red' + piece + '_' + str(i), 'red', piece)

    def generate_init_pos(self):
        j = 0
        for i in range(0, 9, 2):
            self.top_init_pos['soldier_' + str(j)] = (3, i)
            self.bottom_init_pos['soldier_' + str(j)] = (6, i)
            j += 1

        for i in range(0, 4):
            j = 0
            self.top_init_pos[self.piece[i] + '_' + str(j)] = (0, i)
            self.bottom_init_pos[self.piece[i] + '_' + str(j)] = (9, i)
            j += 1
            self.top_init_pos[self.piece[i] + '_' + str(j)] = (0, 8-i)
            self.bottom_init_pos[self.piece[i] + '_' + str(j)] = (9, 8-i)

        self.top_init_pos['general_0'] = (0, 4)
        self.bottom_init_pos['general_0'] = (9, 4)
        self.top_init_pos['cannon_0'] = (2, 1)
        self.bottom_init_pos['cannon_0'] = (7, 1)
        self.top_init_pos['cannon_1'] = (2, 7)
        self.bottom_init_pos['cannon_1'] = (7, 7)

    def init_piece_pos(self):
        if self.top == 'red':
            for key in self.red_pieces.keys():
                self.red_pieces[key].set_init_pos(self.top_init_pos[key])
                self.black_pieces[key].set_init_pos(self.bottom_init_pos[key])

        else:
            for key in self.red_pieces.keys():
                self.red_pieces[key].set_init_pos(self.bottom_init_pos[key])
                self.black_pieces[key].set_init_pos(self.top_init_pos[key])

    def print_pieces(self):
        for key in self.red_pieces.keys():
            print(key + ": " + tuple_to_str(self.red_pieces[key].get_current_pos()))

        print("\n")
        for key in self.black_pieces.keys():
            print(key + ": " + tuple_to_str(self.black_pieces[key].get_current_pos()))

    def init_board(self):
        for i in range(0, 10):
            board_y = []
            for j in range(0, 9):
                board_y.append(self.BOARD_IS_EMPTY)
            self.board.append(board_y)

        for key in self.red_pieces.keys():
            y, x = self.red_pieces[key].get_current_pos()
            self.board[y][x] = self.red_pieces[key]

        for key in self.black_pieces.keys():
            y, x = self.black_pieces[key].get_current_pos()
            self.board[y][x] = self.black_pieces[key]

    def print_board(self):
        for i in range(10):
            for j in range(9):
                sys.stdout.write(self.board[i][j].__str__() + " ")
            print()

    def move(self, cur_pos, new_pos):
        piece = None

        if cur_pos in self.black_pieces:
            piece = self.black_pieces[cur_pos]
        elif cur_pos in self.red_pieces:
            piece = self.red_pieces[cur_pos]
        else:
            # May be raise error message to say that the move is invalid because there is no piece at the
            # current position
            return False

        self.validate(piece, new_pos)
        self.update(piece, new_pos)

    def validate(self, piece, new_pos):
        cur_pos = piece.get_current_pos()
        team = piece.team
        type = piece.type
        pass_river = None

        if type == 'chariot':
            pass
        if type == 'horse':
            pass
        if type == 'cannon':
            pass

        if team == self.top:
            if type == 'soldier':
                pass_river = piece.pass_river
                pass
            if type == 'elephant':
                pass
            if type == 'advisor':
                pass
            if type == 'general':
                pass
        else:
            if type == 'soldier':
                pass_river = piece.pass_river
                pass
            if type == 'elephant':
                pass
            if type == 'advisor':
                pass
            if type == 'general':
                pass

    def update(self, piece, new_pos):
        pass


if __name__ == '__main__':
    game = Game()
    game.print_pieces()
    game.print_board()