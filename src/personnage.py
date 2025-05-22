class Personnage:
    def __init__(self):
        self.hp = 10

    def est_vivant(self):
        return self.hp > 0
    
    def recevoir_attaque(self):
        if self.est_vivant():
            self.hp -= 2 #faux, essai echec test
