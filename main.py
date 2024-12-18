from case import Case
from jeu import Jeu
from joueur import Joueur
from plateau import Plateau
import time
import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

plateau_du_jeu = Plateau()

plateau_du_jeu.creation_cases()

partie = Jeu()
