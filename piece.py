class Piece (object):

    def __init__(self, name, team, piece_type, pos):
        self.name = name
        self.team = team
        self.type = piece_type
        self.his_pos = []
        self.his_pos.append(pos)
        self.pass_river = False

    def move(self, pos):
        self.his_pos.append(pos)

    def get_current_pos(self):
        return self.his_pos[-1]

    def __str__(self):
        x, y = self.get_current_pos()
        #return self.name + ': (' + str(x) + ', ' + str(y) + ')'
        return self.type[0:3]
    def __repr__(self):
        return self.name + ' ' + self.get_current_pos()