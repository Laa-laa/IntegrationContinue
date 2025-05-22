class Personnage:
    def __init__(self, nom):
        self.hp = 10
        self.nom = nom

    def est_vivant(self):
        return self.hp > 0
    
    def recevoir_attaque(self):
        if self.est_vivant():
            self.hp -= 1
        return self.hp > 0
