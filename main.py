from jeu import Jeu
from plateau import Plateau

plateau_du_jeu = Plateau()
plateau_du_jeu.creation_cases()
# plateau_du_jeu.creer_plateau()
partie = Jeu()
partie.lancer_jeu()