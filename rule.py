import re 
import sys 

print("Hello") 
print("How are you")

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
    def __init__(self):
        self._DOMAIN_X = 8
        self._DOMAIN_Y = 9
    
    def is_in_board(self, new_pos):
        if ( pos.x >= 0 and pos.x <= 8)
            and ( pos.y >= 0 and pos.y <= 9):
            return True 
        else : return False 

    def is_interfered(self, board_map, old_pos, new_pos):
        pass 

    def soldier_upper_half(self, old_pos, new_pos): 
        if is_in_board(new_pos): 
            if not is_interfered(board_map, old_pos, new_pos):
                sol = moving_ruleset():
                return sol.soldier_upper_half(old_pos, new_pos)

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
