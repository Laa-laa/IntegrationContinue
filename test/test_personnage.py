from src.personnage import Personnage

def test_nouveau_personnage_a_10_points_de_vie():
    p = Personnage()
    assert p.hp == 10

def test_personnage_est_vivant_par_defaut():
    p = Personnage()
    assert p.est_vivant()

def test_personnage_perd_1_hp_quand_attaque():
    p = Personnage()
    p.recevoir_attaque()
    assert p.hp == 9

def test_personnage_meurt_quand_hp_atteint_zero():
    p = Personnage()
    for _ in range(10):
        p.recevoir_attaque()
    assert not p.est_vivant()


