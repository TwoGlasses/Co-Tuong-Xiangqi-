from piece import Piece

"""
Ruleset for Xiangqi chesspiece: soldier, cannon, chariot, horse, elephant, advisor, general
"""


class Ruleset(object):
    """
    ## Setting down ruleset for chesspieces' movements
    ### Movements of pieces
    Cannon: straight line movement with maximum step of 10 or 9 according to respective axes
    Chariot: straight line movement with maximum step of 10 or 9 according to respective axes
    Horse: L shape movement with the longer stroke takes 2 unit, short stroke takes 1 unit.
    Elephant: Diagonal jump of 2 on x axis and 2 on y axis (pos[0 +/- 2, pos[1 +/- 2) with pos if the elephant position
    Advisor: Diagonal jump of 1 both x and y axis (pos[0 +/- 1, pos[1 +/- 1)
    General: Moving parallel to either axes, 1 unit each time.
    Soldier: Same with general, no going backwards respectively to its general.

    ### Interfering rule: Define how a movement of a chesspiece cannot be carried out.
    Cannon: another piece in its straight pathway
    Chariot: another piece in its straight pathway
    Horse: A piece placed at the middle of the longer stroke
    Elephant: A piece placed at the middle of the diagonal jump (pos[0 +/- 1, pos[1 +/- 1) with pos is the elephant position
    """

    def __init__(self, board_map_2d):
        """
        Define domains of upper area (AREA 1 - Upper half), lower area (AREA 2 - Lower half);
        AREA 1 palace - Northern palace, AREA 2 palace - Southern palace;
        Place-holder for empty position: _IS_EMPTY

        @param board_map_2d
        """

        self._DOMAIN_X = 8
        self._DOMAIN_Y = 9
        self._DOMAIN_X_UPPER_HALF = self._DOMAIN_X_LOWER_HALF = [0, 8]
        self._DOMAIN_X_NORTHERN_PALACE = self._DOMAIN_X_SOUTHERN_PALACE = [3, 5]
        self._DOMAIN_Y_UPPER_HALF = [0, 4]
        self._DOMAIN_Y_LOWER_HALF = [5, 9]
        self._DOMAIN_Y_NORTHERN_PALACE = [0, 2]
        self._DOMAIN_Y_SOUTHERN_PALACE = [7, 9]

        self._IS_EMPTY = '  .  '
        self.board_map_2d = board_map_2d

    def is_in_board(self, pos):
        """
            Check to see if a position is in board or not
        :param pos: A Pos object that conatains a position
        :return: True if the position is in board otherwise returns False
        """

        if 0 <= pos[1] <= 8 and 0 <= pos[0] <= 9:
            return True
        else:
            return False

    def is_in_upper_half(self, pos):
        if (self._DOMAIN_X_UPPER_HALF[0] <= pos[1] <= self._DOMAIN_X_UPPER_HALF[1]) and (
                self._DOMAIN_Y_UPPER_HALF[0] <= pos[0] <= self._DOMAIN_Y_UPPER_HALF[1]):
            return True
        else:
            return False

    def is_in_lower_half(self, pos):
        if (self._DOMAIN_X_LOWER_HALF[0] <= pos[1] <= self._DOMAIN_X_LOWER_HALF[1]) and (
                self._DOMAIN_Y_LOWER_HALF[0] <= pos[0] <= self._DOMAIN_Y_LOWER_HALF[1]):
            return True
        else:
            return False

    def is_in_upper_palace(self, pos):
        if (self._DOMAIN_Y_NORTHERN_PALACE[0] <= pos[1] <= self._DOMAIN_X_NORTHERN_PALACE[1]) and (
                self._DOMAIN_Y_NORTHERN_PALACE[0] <= pos[0] <= self._DOMAIN_Y_NORTHERN_PALACE[1]):
            return True
        else:
            return False

    def is_in_lower_palace(self, pos):
        if (self._DOMAIN_X_SOUTHERN_PALACE[0] <= pos[1] <= self._DOMAIN_X_SOUTHERN_PALACE[1]) and (
                self._DOMAIN_Y_SOUTHERN_PALACE[0] <= pos[0] <= self._DOMAIN_Y_SOUTHERN_PALACE[1]):
            return True
        else:
            return False

    def is_interfered(self, old_pos, new_pos):
        the_one = ['horse', 'elephant', 'cannon', 'chariot']
        if self.get_piece(old_pos).type in the_one:
            if self.get_piece(old_pos).type == the_one[0]:
                return self.board_map_2d[new_pos[0]][new_pos[1]] != self._IS_EMPTY or self.is_interfered_horse(old_pos,
                                                                                                             new_pos)
            elif self.get_piece(old_pos).type == the_one[1]:
                return self.board_map_2d[new_pos[0]][new_pos[1]] != self._IS_EMPTY or self.is_interfered_elephant(old_pos,
                                                                                                                new_pos)
            elif self.get_piece(old_pos).type == the_one[2]:
                return self.board_map_2d[new_pos[0]][new_pos[1]] != self._IS_EMPTY or self.is_interfered_cannon(old_pos,
                                                                                                              new_pos)
            elif self.get_piece(old_pos).type == the_one[3]:
                return self.board_map_2d[new_pos[0]][new_pos[1]] != self._IS_EMPTY or self.is_interfered_chariot(old_pos,
                                                                                                               new_pos)
            else:
                raise ValueError('MovRuleSpecial_5: Unknown piece. Piece is not either horse or elephant.')
        else:
            return self.board_map_2d[new_pos[0]][new_pos[1]] != self._IS_EMPTY

    def is_interfered_horse(self, old_pos, new_pos):
        buffer_x = new_pos[1] - old_pos[1]
        buffer_y = new_pos[0] - old_pos[0]
        ki_da = Pos()
        if buffer_y == 2:
            ki_da.y = old_pos[0] + buffer_y - 1
        elif buffer_y == -2:
            ki_da.y = old_pos[0] + buffer_y + 1
        elif abs(buffer_y) == 1:
            ki_da.y = old_pos[0]
        else:
            return False

        if buffer_x == 2:
            ki_da.x = old_pos[1] + buffer_x - 1
        elif buffer_x == -2:
            ki_da.x = old_pos[1] + buffer_x + 1
        elif abs(buffer_x) == 1:
            ki_da.x = old_pos[1]
        else:
            return False

        return self.board_map_2d[ki_da.y][ki_da.x] != self._IS_EMPTY

    def is_interfered_elephant(self, old_pos, new_pos):
        return self.board_map_2d[old_pos[0] + int((new_pos[0] - old_pos[0]) / 2)][
                   old_pos[1] + int((new_pos[1] - old_pos[1]) / 2)] != self._IS_EMPTY

    def is_interfered_cannon(self, old_pos, new_pos, eat=False):
        check_list = []
        if old_pos[1] == new_pos[1]:
            if old_pos[0] > new_pos[0]:
                check_list = [self.board_map_2d[index][old_pos[1]] for index in range(new_pos[0], old_pos[0] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
            else:
                check_list = [self.board_map_2d[index][old_pos[1]] for index in range(old_pos[0], new_pos[0] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
        elif old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                check_list = [self.board_map_2d[old_pos[0]][index] for index in range(new_pos[1], old_pos[1] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
            else:
                check_list = [self.board_map_2d[old_pos[0]][index] for index in range(old_pos[1], new_pos[1] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
        else:
            raise ValueError('MovRuleSpecial_9: Nonsense in position of cannon.')

        if not eat:
            if not check_list:
                return True
            else:
                return False
        else:
            if len(check_list) == 1:
                return True
            else:
                return False

    def is_interfered_chariot(self, old_pos, new_pos):
        check_list = []
        if old_pos[1] == new_pos[1]:
            if old_pos[0] > new_pos[0]:
                check_list = [self.board_map_2d[index][old_pos[1]] for index in range(new_pos[0], old_pos[0] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
            else:
                check_list = [self.board_map_2d[index][old_pos[1]] for index in range(old_pos[0], new_pos[0] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
        elif old_pos[0] == new_pos[0]:
            if old_pos[1] > new_pos[1]:
                check_list = [self.board_map_2d[old_pos[0]][index] for index in range(new_pos[1], old_pos[1] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
            else:
                check_list = [self.board_map_2d[old_pos[0]][index] for index in range(old_pos[1], new_pos[1] + 1) if
                              self.board_map_2d[index][old_pos[1]] != self._IS_EMPTY]
        else:
            raise ValueError('MovRuleSpecial_10: Nonsense in position of chariot.')

        if check_list:
            return False
        else:
            return True

    def is_enemy(self, Piece_1, Piece_2):
        return Piece_1.team != Piece_2.team

    def get_piece(self, pos):
        return self.board_map_2d[pos[0]][pos[1]]

    def soldier(self, old_pos, new_pos):
        piece = self.get_piece(old_pos)
        if piece.pass_river:
            if self.is_in_lower_half(old_pos):
                return self.soldier_passed_river_upper_half(old_pos, new_pos)
            else:
                return self.soldier_passed_river_lower_half(old_pos, new_pos)
        else:
            if self.is_in_lower_half(old_pos):
                return self.soldier_lower_half(old_pos, new_pos)
            else:
                return self.soldier_upper_half(old_pos, new_pos)

    def soldier_upper_half(self, old_pos, new_pos):
        """
        Soldier from the upper country
        """

        if new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == 1:
            return True
        else:
            return False

    def soldier_lower_half(self, old_pos, new_pos):
        """
        Soldier from the lower country
        """
        if new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == -1:
            return True
        else:
            return False

    def soldier_passed_river_upper_half(self, old_pos, new_pos):
        """
        Soldier from the upper country moves in the lower country
        """
        if (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == 1) or \
                (new_pos[1] - old_pos[1] == 1 and new_pos[0] - old_pos[0] == 0) or \
                (new_pos[1] - old_pos[1] == -1 and new_pos[0] - old_pos[0] == 0):  # Going to the right
            return True
        else:
            return False

    def soldier_passed_river_lower_half(self, old_pos, new_pos):
        """
        Soldier from the lower country moves in the upper country
        """
        if (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == -1) or \
                (new_pos[1] - old_pos[1] == 1 and new_pos[0] - old_pos[0] == 0) or \
                (new_pos[1] - old_pos[1] == -1 and new_pos[0] - old_pos[0] == 0):  # Going to the right
            return True
        else:
            return False

    def elephant(self, old_pos, new_pos):
        if self.is_in_lower_half(old_pos):
            if self.is_in_lower_half(new_pos):
                if abs(new_pos[1] - old_pos[1]) == 2 and abs(new_pos[0] - old_pos[0]) == 2:
                    return True
        elif self.is_in_upper_half(old_pos):
            if self.is_in_upper_half(new_pos):
                return True
        return False

    def advisor(self, old_pos, new_pos):
        if self.is_in_lower_palace(old_pos):
            if self.is_in_lower_palace(new_pos):
                if abs(new_pos[1] - old_pos[1]) == 1 and abs(new_pos[0] - old_pos[0]) == 1:
                    return True
        elif self.is_in_upper_palace(old_pos):
            if self.is_in_upper_palace(new_pos):
                if abs(new_pos[1] - old_pos[1]) == 1 and abs(new_pos[0] - old_pos[0]) == 1:
                    return True
        return False

    def general(self, old_pos, new_pos):
        if self.is_in_lower_palace(old_pos):
            if self.is_in_lower_palace(new_pos):
                if (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == 1) or \
                        (new_pos[1] - old_pos[1] == 1 and new_pos[0] - old_pos[0] == 0) or \
                        (new_pos[1] - old_pos[1] == -1 and new_pos[0] - old_pos[0] == 0) or \
                        (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == -1):  # Going back
                    return True
        elif self.is_in_upper_palace(old_pos):
            if self.is_in_upper_palace(new_pos):
                if (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == 1) or \
                        (new_pos[1] - old_pos[1] == 1 and new_pos[0] - old_pos[0] == 0) or \
                        (new_pos[1] - old_pos[1] == -1 and new_pos[0] - old_pos[0] == 0) or \
                        (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] == -1):  # Going back
                    return True
        return False

    def horse(self, old_pos, new_pos):
        if (abs(new_pos[1] - old_pos[1]) == 2 and abs(new_pos[0] - old_pos[0]) == 1) \
                or (abs(new_pos[1] - old_pos[1]) == 1 and abs(new_pos[0] - old_pos[0]) == 2):
            return True
        else:
            return False

    def chariot(self, old_pos, new_pos):
        if (new_pos[1] - old_pos[1] != 0 and new_pos[0] - old_pos[0] == 0) \
                or (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] != 0):
            return True
        else:
            return False

    def cannon(self, old_pos, new_pos):
        if (new_pos[1] - old_pos[1] != 0 and new_pos[0] - old_pos[0] == 0) or \
                (new_pos[1] - old_pos[1] == 0 and new_pos[0] - old_pos[0] != 0):
            return True
        else:
            return False

    def get_eaten(self, eater, old_pos, new_pos):
        self.board_map_2d[new_pos[0]][new_pos[1]] = eater
        self.board_map_2d[old_pos[0]][old_pos[1]] = self._IS_EMPTY

    def can_I_eat_this(self, old_pos, new_pos):
        the_ones = ['cannon', 'elephant', 'horse', 'chariot']
        if self.get_piece(old_pos).type not in the_ones:
            return True
        elif self.get_piece(old_pos).type == the_ones[0]:
            return self.is_interfered_cannon(old_pos, new_pos, eat=True)
        elif self.get_piece(old_pos).type == the_ones[1]:
            return self.is_interfered_elephant(old_pos, new_pos)
        elif self.get_piece(old_pos).type == the_ones[2]:
            return self.is_interfered_horse(old_pos, new_pos)
        elif self.get_piece(old_pos).type == the_ones[3]:
            return self.is_interfered_chariot(old_pos, new_pos)
        else:
            raise ValueError('MovRuleSpecial_8: Unknown chesspiece.')

    def move_allowed(self, old_pos, new_pos):
        """
            Check whether a move is allowed
        """

        if new_pos[1] == old_pos[1] and new_pos[0] == old_pos[0]:
            return True
        elif self.is_in_board(new_pos):
            if not self.is_interfered(old_pos, new_pos):
                if self.get_piece(old_pos).type != 'soldier':
                    return getattr(Ruleset, self.get_piece(old_pos).type)(old_pos,
                                                                          new_pos) and self.you_shall_not_pass(
                        old_pos, new_pos)
                elif self.get_piece(old_pos).pass_river:
                    if self.is_in_upper_half(self.get_piece(old_pos).his_pos[1]):
                        return self.soldier_passed_river_upper_half(old_pos, new_pos)
                    elif self.is_in_lower_half(self.get_piece(old_pos).his_pos[1]):
                        return self.soldier_passed_river_lower_half(old_pos, new_pos)
                    else:
                        raise ValueError('MovRuleSpecial_6: Unknown soldier position with Piece.pass_river = True')
                else:
                    if self.is_in_upper_half(self.get_piece(old_pos).his_pos[1]):
                        return self.soldier_upper_half(old_pos, new_pos)
                    elif self.is_in_lower_half(self.get_piece(old_pos).his_pos[1]):
                        return self.soldier_lower_half(old_pos, new_pos)
                    else:
                        raise ValueError('MovRuleSpecial_7: Unknown soldier position with Piece.pass_river = False')
            elif self.is_enemy(self.get_piece(old_pos), self.get_piece(new_pos)):
                # Update the map, the occupant get replaced by the new piece
                if self.can_I_eat_this(old_pos, new_pos):
                    self.get_eaten(self.get_piece(old_pos), old_pos, new_pos)
            else:
                return False
        else:
            return False


