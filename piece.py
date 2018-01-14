class Piece(object):
    def __init__(self, name, team, piece_type):
        self.name = name
        self.team = team
        self.type = piece_type
        self.his_pos = []
        self.pass_river = False
        self.nick_name = team[0] + '_' + self.type[0:3] + '_' + self.name[-1]

    def set_init_pos(self, pos):
        self.his_pos.append(pos)

    def move(self, pos):
        self.his_pos.append(pos)

    def get_current_pos(self):
        return self.his_pos[-1]

    def __str__(self):
        return self.nick_name

    def __repr__(self):
        return self.name