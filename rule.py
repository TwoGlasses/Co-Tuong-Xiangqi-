from piece import Piece  

''' 
Ruleset for Xiangqi chesspiece: soldier, cannon, chariot, horse, elephant, advisor, general 
''' 

class Pos(object):

    '''
    A class for storing position of chess piece
    ''' 

    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
class ruleset(object): 

    '''
    ### Setting move ruleset class
    Cannon, Chariot : straight line movement with maximum step of 10 or 9 according to respective axes
    Horse: L shape movement with the longer stroke takes 2 unit, short stroke takes 1 unit.

    Interfering rule: 
    __ Define how a movement of a chesspiece cannot be carried out __
    Canon, Chariot : straight line movement will be 

    '''

    def __init__(self, board_map_2d):
        self._DOMAIN_X = 8
        self._DOMAIN_Y = 9
        self._IS_EMPTY = '  .  '
        self.board_map_2d = board_map_2d
    
    def is_in_board(self, new_pos):
        if ( pos.x >= 0 and pos.x <= 8)
            and ( pos.y >= 0 and pos.y <= 9):
            return True 
        else : return False 

    def is_interfered(self, old_pos, new_pos):
        return board_map[new_pos.y][new_pos.x] != self._IS_EMPTY

    def is_enemy(self, Piece_1, Piece_2):
        return Piece_1.team != Piece_2.team

    def get_piece(self, pos):
        return self.board_map_2d[pos.y][pos.x]

    def get_eaten(self, eater, pos): 
        eater = self.board_map_2d[pos.y][pos.x]

    def soldier_upper_half(self, old_pos, new_pos): 
        if is_in_board(new_pos): 
            if not is_interfered(board_map, old_pos, new_pos):
                sol = moving_ruleset():
                return sol.soldier_upper_half(old_pos, new_pos)
            elif is_enemy(self.get_piece(old_pos), self.get_piece(new_pos)): 
                #Update the map, the occupant get replaced by the new piece 
                self.get_eaten(self.get_piece(old_pos), new_pos)
                


    def soldier_lower_half(self, old_pos, new_pos):
        pass 

    def soldier_passed_river_upper_half(self, old_pos, new_pos):
        pass 

    def soldier_passed_river_lower_half(self, old_pos, new_pos):
        pass

    def cannon(self, old_pos, new_pos):
        pass 

    def chariot(self, old_pos, new_pos):
        pass 
    
    def horse(self, old_pos, new_pos):
        pass
    
    def elephant(self, old_pos, new_pos):
        pass 

    def advisor(self, old_pos, new_pos):
        pass 

    def general(self, old_pos, new_pos):
        pass 

class moving_ruleset(object):
    '''
    Checking movement of chess piece
    Not checking in_board and get_interfered
    ''' 

    def soldier_upper_half(self, old_pos, new_pos):
        if new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1: 
            return True 
        else : return False 

    def soldier_lower_half(self, old_pos, new_pos): 
        if new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1:
            return True 
        else: return False

    def soldier_passed_river_upper_half(self, old_pos, new_pos): 
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1 ) #Going forth     
            or ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) #Going to the left
                or ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ): #Going to the right
            return True 
        else: return False

    def soldier_passed_river_lower_half(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1 ) #Going forth     
            or ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) #Going to the left
                or ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ): #Going to the right
            return True 
        else: return False

    def cannon(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x != 0 and new_pos.y -  old_pos.y == 0)
            or ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y != 0):
            return True 
        else: return False 

    def advisor(self, old_pos, new_pos):
        if abs(new_pos.x - old_pos.x) == 1 and abs(new_pos.y -old_pos.y) == 1:
            return True
        else: return False 

    def general(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == 1 ) #Going forth     
            or ( new_pos.x - old_pos.x == 1 and new_pos.y - old.pos.y == 0) #Going to the left
                or ( new_pos.x - old_pos.x == -1 and new_pos.y - old_pos.y == 0 ) #Going to the right
                    or ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y == -1)#Going back 
            return True 
        else: return False 

    def horse(self, old_pos, new_pos):
        if ( abs(new_pos.x - old_pos.x) == 2 and abs(new_pos.y - old_pos.y) == 1 )
            or ( abs(new_pos.x - old_pos.x) == 1 and abs(new_pos.y - old_pos.y) == 2):
            return True
        else: return False

    def chariot(self, old_pos, new_pos):
        if ( new_pos.x - old_pos.x != 0 and new_pos.y -  old_pos.y == 0)
            or ( new_pos.x - old_pos.x == 0 and new_pos.y - old_pos.y != 0):
            return True 
        else: return False 

    def elephant(self, old_pos, new_pos):
        if abs( new_pos.x - old_pos.x) == 2 and abs( new_pos.y - old_pos.y) == 2:
            return True 
        else: return False 
