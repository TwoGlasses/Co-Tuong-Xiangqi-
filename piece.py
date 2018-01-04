class Piece:
    name = None
    team = None
    type = None
    his_pos = None
    pass_river = None

    def piece(self, name, team, piece_type):
        self.name = name
        self.team = team
        self.type = piece_type
        self.his_pos = []
        self.pass_river = False

    def get_current_pos(self):
        return self.his_pos[-1]

    @get_team
    def get_team(self):
        return self.team