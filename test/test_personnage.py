from src.personnage import Personnage

def test_nouveau_personnage_a_10_points_de_vie():
    p = Personnage()
    assert p.hp == 10

def test_personnage_est_vivant_par_defaut():
    p = Personnage()
    assert p.est_vivant()