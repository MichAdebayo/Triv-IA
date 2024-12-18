import random

class Joueur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.camemberts = set()  # Ensemble pour stocker les couleurs de camemberts gagnés
        self.position = 0  # Position actuelle du joueur sur le plateau

    def ajouter_camembert(self, couleur):
        """Ajoute un camembert de couleur spécifique au joueur."""
        self.camemberts.add(couleur)
        print(f"{self.nom} a gagné un camembert de couleur {couleur} !")

    def a_tous_les_camemberts(self):
        """Vérifie si le joueur a collecté les 6 camemberts."""
        return len(self.camemberts) == 6

    def lancer_de(self):
        """Simule le lancer du dé."""
        return random.randint(1, 6)
