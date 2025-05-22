from src.personnage import Personnage

def test_nouveau_personnage_a_10_points_de_vie():
    p = Personnage("Test")
    assert p.hp == 10

def test_personnage_est_vivant_par_defaut():
    p = Personnage("Test")
    assert p.est_vivant()

def test_personnage_perd_1_hp_quand_attaque():
    p = Personnage("Test")
    p.recevoir_attaque()
    assert p.hp == 9

def test_personnage_meurt_quand_hp_atteint_zero():
    p = Personnage("Test")
    for _ in range(10):
        p.recevoir_attaque()
    assert not p.est_vivant()

def test_initialisation_personnage_nom_et_hp():
    p = Personnage("Link")
    
    assert p.nom == "Link"
    assert p.hp == 10


