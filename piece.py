class Piece(object):
    """
        A class for storing information about a piece in the chess game. The attribute that needs to be store are:
        name: Name of the piece
        team: Team of the piece (black or red)
        type: Type of the piece
        his_pos: A list that stores all the moves of the piece
        pass_river: A boolean value states whether the piece has passed the river of not (for soldier type)
        nick_name: A nickname to display on the CLI board
    """
    def __init__(self, name, team, piece_type):
        """
            A constructor for Piece class

        :param name: The name of the piece
        :param team: The team that the piece belongs to (black or red)
        :param piece_type: The type of piece
        """
        self.name = name
        self.team = team
        self.type = piece_type
        self.his_pos = []
        self.pass_river = False
        self.nick_name = team[0] + '_' + self.type[0:3] + '_' + self.name[-1]

    def set_init_pos(self, pos):
        """
            A method to initiate the pos of the piece. This is separate from the __init__() because of the way
            the piece is initiated

        :param pos: The initial position of the piece
        """
        self.his_pos.append(pos)

    def move(self, pos):
        """
            A method to change the position of the piece

        :param pos: the new position for the piece
        """
        self.his_pos.append(pos)

    def get_current_pos(self):
        """
            A method to get the current position of the piece

        :return: current position of the piece
        """
        return self.his_pos[-1]

    def __str__(self):
        """
           A method to display the piece as a string
        :return: The nickname to represent the piece
        """
        return self.nick_name

