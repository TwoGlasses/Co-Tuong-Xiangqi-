from piece import Piece  

'''
Ruleset for Xiangqi chesspiece: soldier, cannon, chariot, horse, elephant, advisor, general
'''

class Pos(object):

    '''
    A class for storing position of chess piece
    ''' 

    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y 
    
class ruleset(object): 

    '''
    ## Setting down ruleset for chesspieces' movements
    ### Movements of pieces
    Cannon: straight line movement with maximum step of 10 or 9 according to respective axes
    Chariot: straight line movement with maximum step of 10 or 9 according to respective axes
    Horse: L shape movement with the longer stroke takes 2 unit, short stroke takes 1 unit.
    Elephant: Diagonal jump of 2 on x axis and 2 on y axis (pos.x +/- 2, pos.y +/- 2) with pos if the elephant position
    Advisor: Diagonal jump of 1 both x and y axis (pos.x +/- 1, pos.y +/- 1)
    General: Moving parallel to either axes, 1 unit each time. 
    Soldier: Same with general, no going backwards respectively to its general.
    
    ### Interfering rule: Define how a movement of a chesspiece cannot be carried out.
    Cannon: another piece in its straight pathway 
    Chariot: another piece in its straight pathway 
    Horse: A piece placed at the middle of the longer stroke 
    Elephant: A piece placed at the middle of the diagonal jump (pos.x +/- 1, pos.y +/- 1) with pos is the elephant position
    
    
    '''

    def __init__(self, board_map_2d):
        '''
        Define domains of upper area (AREA 1 - Upper half), lower area (AREA 2 - Lower half); 
        AREA 1 palace - Northern palace, AREA 2 palace - Southern palace;
        Place-holder for empty position: _IS_EMPTY 

        @param board_map_2d 
        '''
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
        if ( pos.x >= 0 and pos.x <= 8) and ( pos.y >= 0 and pos.y <= 9):
            return True 
        else : return False 

    def is_in_upper_half(self, pos):
        if ( pos.x >= self._DOMAIN_X_UPPER_HALF[0] and pos.x <= self._DOMAIN_X_UPPER_HALF[1]) and ( pos.y >= self._DOMAIN_Y_UPPER_HALF[0] and pos.y <= self._DOMAIN_Y_UPPER_HALF[1]):
            return True 
        else : return False 
    
    def is_in_lower_half(self, pos):
        if ( pos.x >= self._DOMAIN_X_LOWER_HALF[0] and pos.x <= self._DOMAIN_X_LOWER_HALF[1]) and ( pos.y >= self._DOMAIN_Y_LOWER_HALF[0] and pos.y <= self._DOMAIN_Y_LOWER_HALF[1]):
            return True 
        else : return False 

    def is_in_northern_palace(self, pos):
        if ( pos.x >= self._DOMAIN_Y_NORTHERN_PALACE[0] and pos.x <= self._DOMAIN_X_NORTHERN_PALACE[1]) and ( pos.y >= self._DOMAIN_Y_NORTHERN_PALACE[0] and pos.y <= self._DOMAIN_Y_NORTHERN_PALACE[1]):
            return True 
        else : return False 

    def is_in_southern_palace(self, pos):
        if ( pos.x >= self._DOMAIN_X_SOUTHERN_PALACE[0] and pos.x <= self._DOMAIN_X_SOUTHERN_PALACE[1]) and ( pos.y >= self._DOMAIN_Y_SOUTHERN_PALACE[0] and pos.y <= self._DOMAIN_Y_SOUTHERN_PALACE[1]):
            return True 
        else : return False 

    def you_shall_not_pass(self, old_pos, new_pos):
        '''
        Determine if piece is in the group of elephant , advisor, general and apply its special rule of not leaving palace or country respectively
        '''

        imperial_guard = ['elephant', 'advisor', 'general']
        the_one = self.get_piece(old_pos).type 
        if the_one in imperial_guard: 
            the_origin_coords = the_one.his_pos[-1]            
            if the_one == imperial_guard[0]: 
                if self.is_in_lower_half(the_origin_coords): 
                    return self.is_in_lower_half(new_pos)
                elif self.is_in_upper_half(the_origin_coords): 
                    return self.is_in_upper_half(new_pos)
                else: 
                    raise ValueError('The Elephant is travelling oversea!!! MovRuleSpecial_1: Chesspiece is not detected in board')
            elif the_one == imperial_guard[1]: 
                if self.is_in_northern_palace(the_origin_coords):
                    return self.is_in_northern_palace(new_pos)
                elif self.is_in_southern_palace(the_origin_coords):
                    return self.is_in_southern_palace(new_pos)
                else: 
                    raise ValueError('Advisor not detected in the palace!!! MovRuleSpecial_2: Chesspiece is not detected in both palaces')
            elif the_one == imperial_guard[2]: 
                if self.is_in_southern_palace(the_origin_coords):
                    return self.is_in_southern_palace(new_pos)
                elif self.is_in_northern_palace(the_origin_coords): 
                    return self.is_in_northern_palace(new_pos)
                else: 
                    raise ValueError('This is bad, the General is missing in the palace!!! MovRuleSpecial_3: Chesspiece is not detected in both palaces')
            else: 
                raise ValueError('What is the world is this thing? Identify thyself!! MovRuleSpecial_4: Chesspiece does not belong to the special group')

    def to_be_or_not_to_be(self, old_pos, new_pos): 
        '''
        Determine if the soldier has passed the river and apply moving rule accordingly 
        '''
        pass 

    def is_interfered(self, old_pos, new_pos):
        the_one = ['horse', 'elephant', 'cannon', 'chariot']
        if self.get_piece(old_pos).type in the_one:  
            if self.get_piece(old_pos).type == the_one[0]: 
                return self.board_map_2d[new_pos.y][new_pos.x] != self._IS_EMPTY or self.is_interfered_horse(old_pos, new_pos)
            elif self.get_piece(old_pos).type == the_one[1]:
                return self.board_map_2d[new_pos.y][new_pos.x] != self._IS_EMPTY or self.is_interfered_elephant(old_pos, new_pos)
            elif self.get_piece(old_pos).type == the_one[2]: 
                return self.board_map_2d[new_pos.y][new_pos.x] != self._IS_EMPTY or self.is_interfered_cannon(old_pos, new_pos)
            elif self.get_piece(old_pos).type == the_one[3]:
                return self.board_map_2d[new_pos.y][new_pos.x] != self._IS_EMPTY or self.is_interfered_chariot(old_pos, new_pos)
            else:
                raise ValueError('MovRuleSpecial_5: Unknown piece. Piece is not either horse or elephant.')
        else:
            return self.board_map_2d[new_pos.y][new_pos.x] != self._IS_EMPTY

    def is_interfered_horse(self, old_pos, new_pos):
        buffer_x = new_pos.x - old_pos.x
        buffer_y = new_pos.y - old_pos.y
        ki_da    = Pos()
        if buffer_y == 2: 
            ki_da.y = old_pos.y + buffer_y - 1
        elif buffer_y == -2: 
            ki_da.y = old_pos.y + buffer_y + 1
        elif abs(buffer_y) == 1: 
            ki_da.y = old_pos.x 
        else: 
            return False 

        if buffer_x == 2: 
            ki_da.x = old_pos.x + buffer_x - 1
        elif buffer_x == -2:
            ki_da.x = old_pos.x + buffer_x + 1    
        elif abs(buffer_x) == 1: 
            ki_da.x = old_pos.x 
        else: 
            return False 
        
        return self.board_map_2d[ki_da.y][ki_da.x] == self._IS_EMPTY 

    def is_interfered_elephant(self, old_pos, new_pos):
        return self.board_map_2d[old_pos.y + int((new_pos.y - old_pos.y)/2)][old_pos.x + int((new_pos.x - old_pos.x)/2)] == self._IS_EMPTY

    def is_interfered_cannon(self, old_pos, new_pos, eat = False):
        check_list = []
        if old_pos.x == new_pos.x : 
            if old_pos.y > new_pos.y:
                check_list = [ self.board_map_2d[index][old_pos.x] for  index in range(new_pos.y, old_pos.y + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
            else: 
                check_list = [ self.board_map_2d[index][old_pos.x] for  index in range(old_pos.y, new_pos.y + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
        elif old_pos.y == new_pos.y: 
            if old_pos.x > new_pos.x:
                check_list = [ self.board_map_2d[old_pos.y][index] for  index in range(new_pos.x, old_pos.x + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
            else: 
                check_list = [ self.board_map_2d[old_pos.y][index] for  index in range(old_pos.x, new_pos.x + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
        else: 
            raise ValueError('MovRuleSpecial_9: Nonsense in position of cannon.')

        if not eat:
            if check_list == []:
                return True
            else: return False 
        else: 
            if len(check_list) == 1: 
                return True
            else: return False


    def is_interfered_chariot(self, old_pos, new_pos):
        check_list = []
        if old_pos.x == new_pos.x : 
            if old_pos.y > new_pos.y:
                check_list = [ self.board_map_2d[index][old_pos.x] for  index in range(new_pos.y, old_pos.y + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
            else: 
                check_list = [ self.board_map_2d[index][old_pos.x] for  index in range(old_pos.y, new_pos.y + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
        elif old_pos.y == new_pos.y: 
            if old_pos.x > new_pos.x:
                check_list = [ self.board_map_2d[old_pos.y][index] for  index in range(new_pos.x, old_pos.x + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
            else: 
                check_list = [ self.board_map_2d[old_pos.y][index] for  index in range(old_pos.x, new_pos.x + 1) if self.board_map_2d[index][old_pos.x] != self._IS_EMPTY]
        else: 
            raise ValueError('MovRuleSpecial_10: Nonsense in position of chariot.')

        if check_list != []:
            return False
        else: 
            return True 

    def is_enemy(self, Piece_1, Piece_2):
        return Piece_1.team != Piece_2.team

    def get_piece(self, pos):
        return self.board_map_2d[pos.y][pos.x]

    def get_eaten(self, eater, old_pos, new_pos): 
        self.board_map_2d[new_pos.y][new_pos.x] = eater 
        self.board_map_2d[old_pos.y][old_pos.x] = self._IS_EMPTY

    def can_I_eat_this(self, old_pos, new_pos): 
        the_ones = ['cannon', 'elephant', 'horse','chariot']
        if self.get_piece(old_pos).type not in the_ones: 
            return True 
        elif self.get_piece(old_pos).type == the_ones[0]: 
            return self.is_interfered_cannon(old_pos, new_pos, eat = True)
        elif self.get_piece(old_pos).type == the_ones[1]:
            return self.is_interfered_elephant(old_pos, new_pos)
        elif self.get_piece(old_pos).type == the_ones[2]:
            return self.is_interfered_horse(old_pos, new_pos)
        elif self.get_piece(old_pos).type == the_ones[3]:
            return self.is_interfered_chariot(old_pos, new_pos)
        else: 
            raise ValueError('MovRuleSpecial_8: Unknown chesspiece.')


    def move_allowed(self, old_pos, new_pos): 
        '''
        Call functions from moving_ruleset by the names.
        '''
        if new_pos.x == old_pos.x and new_pos.y == old_pos.y: 
            return True 
        elif is_in_board(new_pos): 
            if not is_interfered(board_map, old_pos, new_pos):
                if self.get_piece(old_pos).type != 'soldier':
                    return  getattr(moving_ruleset, self.get_piece(old_pos).type)(old_pos, new_pos) and self.you_shall_not_pass(old_pos, new_pos)
                elif self.get_piece(old_pos).pass_river: 
                    if self.is_in_upper_half(self.get_piece(old_pos).his_pos[0]):
                        return moving_ruleset.soldier_passed_river_upper_half(old_pos, new_pos)
                    elif self.is_in_lower_half(self.get_piece(old_pos).his_pos[0]):
                        return moving_ruleset.soldier_passed_river_lower_half(old_pos, new_pos)
                    else: 
                        raise ValueError('MovRuleSpecial_6: Unknown soldier position with Piece.pass_river = True')
                else: 
                    if self.is_in_upper_half(self.get_piece(old_pos).his_pos[0]):
                        return moving_ruleset.soldier_upper_half(old_pos, new_pos)
                    elif self.is_in_lower_half(self.get_piece(old_pos).his_pos[0]):
                        return moving_ruleset.soldier_lower_half(old_pos, new_pos)
                    else: 
                        raise ValueError('MovRuleSpecial_7: Unknown soldier position with Piece.pass_river = False')
            elif is_enemy(self.get_piece(old_pos), self.get_piece(new_pos)): 
                #Update the map, the occupant get replaced by the new piece
                if self.can_I_eat_this(old_pos, new_pos) : 
                    self.get_eaten(self.get_piece(old_pos), old_pos, new_pos)
            else: return False 
        else: return False 

class moving_ruleset(object):
    '''
    Checking movement of chess piece
    Not checking in_board and get_interfered
    ''' 

    def __init__(self):
        pass

    def soldier_upper_half(self, old_pos, new_pos):
        '''
        Soldier from the northern country 
        '''
        if new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1: 
            return True 
        else : return False 

    def soldier_lower_half(self, old_pos, new_pos): 
        '''
        Soldier from the southern country 
        '''
        if new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1:
            return True 
        else: return False

    def soldier_passed_river_upper_half(self, old_pos, new_pos): 
        '''
        Soldier from the northern country moves in the southern country 
        '''
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1 ) or  \
            ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) or \
                ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ): #Going to the right
            return True 
        else: return False

    def soldier_passed_river_lower_half(self, old_pos, new_pos):
        '''
        Soldier from the southern country moves in the northern country
        '''
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1 ) or \
            ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) or \
                ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ): #Going to the right
            return True 
        else: return False

    def cannon(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x != 0 and new_pos.y -  old_pos.y == 0) or \
            ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y != 0):
            return True 
        else: return False 

    def advisor(self, old_pos, new_pos):
        if abs(new_pos.x - old_pos.x) == 1 and abs(new_pos.y -old_pos.y) == 1:
            return True
        else: return False 

    def general(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1 ) or \
            ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) or \
                ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ) or \
                    ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1): #Going back 
            return True 
        else: return False 

    def horse(self, old_pos, new_pos):
        if ( abs(new_pos.x - old_pos.x) == 2 and abs(new_pos.y - old_pos.y) == 1 )\
            or ( abs(new_pos.x - old_pos.x) == 1 and abs(new_pos.y - old_pos.y) == 2):
            return True
        else: return False

    def chariot(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x != 0 and new_pos.y -  old_pos.y == 0) \
            or ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y != 0):
            return True 
        else: return False 

    def elephant(self, old_pos, new_pos):
        if abs( new_pos.x - old_pos.x) == 2 and abs( new_pos.y - old_pos.y) == 2:
            return True 
        else: return False 
