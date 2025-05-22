class Personnage:
    def __init__(self):
        self.hp = 10

    def est_vivant(self):
        return self.hp > 0