import random
import json

class Joueur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.camemberts = set()
        self.position = 0

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


class Case:
    def __init__(self, couleur, categorie="Général", camembert=False):
        self.couleur = couleur
        self.categorie = categorie
        self.camembert = camembert

    def __str__(self):
        return f"Case {self.couleur} ({self.categorie})"

class Plateau:
    def __init__(self, nombre_cases=40):
        self.nombre_cases = nombre_cases
        self.couleurs = ["bleu", "rose", "jaune", "vert", "orange", "violet"]
        self.categories = {
            "bleu": "Bases de données",
            "vert": "Python",
            "jaune": "Actualités IA",
            "rose": "Lignes de commandes: Unix",
            "violet": "Personnalités de l'IA",
            "orange": "DevOps"
        }
        self.cases = self.generer_plateau()

    def generer_plateau(self):
        """Génère un plateau avec 6 cases camemberts bien réparties."""
        plateau = []
        indices_camemberts = set(
            i * (self.nombre_cases // len(self.couleurs))
            for i in range(len(self.couleurs))
        )

        for i in range(self.nombre_cases):
            couleur = self.couleurs[i % len(self.couleurs)]
            categorie = self.categories[couleur]  # Use self.categories here

            # Vérifie si cette position est une case camembert
            camembert = i in indices_camemberts

            plateau.append(Case(couleur, categorie=categorie, camembert=camembert))  # Pass categorie and camembert as keyword arguments

        return plateau

    def obtenir_case(self, position): # Added the missing method
        """Retourne la case sur laquelle un joueur arrive."""
        return self.cases[position % self.nombre_cases]



class Questions:
    def __init__(self, question, reponses, bonne_reponse_index, categorie):
        self.question = question
        self.reponses = reponses
        self.bonne_reponse_index = bonne_reponse_index
        self.categorie = categorie

    def poser(self):
        """Pose la question au joueur et retourne s'il a répondu correctement."""
        print(f"\nQuestion ({self.categorie}): {self.question}")
        for i, reponse in enumerate(self.reponses, 1):
            print(f"{i}. {reponse}")

        choix = input("Votre réponse (numéro) : ")
        while not choix.isdigit() or not (1 <= int(choix) <= len(self.reponses)):
            print("Entrée invalide. Réessayez.")
            choix = input("Votre réponse (numéro) : ")

        return int(choix) - 1 == self.bonne_reponse_index


class Jeu:
    def __init__(self):
        self.joueurs = []
        self.questions_par_theme = {}
        self.tour_actuel = 0
        self.plateau = Plateau()

    def initialiser_joueurs(self):
        """Initialise les joueurs avec leurs noms et âges."""
        nb_joueurs = int(input("Entrez le nombre de joueurs (entre 2 et 6) : "))
        while nb_joueurs < 2 or nb_joueurs > 6:
            nb_joueurs = int(input("Entrez un nombre valide (entre 2 et 6) : "))

        for i in range(nb_joueurs):
            nom = input(f"Entrez le nom du joueur {i + 1} : ")
            age = int(input(f"Entrez l'âge de {nom} : "))
            self.joueurs.append(Joueur(nom, age))

    def charger_questions(self, fichier_json):
        """Charge les questions depuis un fichier JSON."""
        with open(fichier_json, "r", encoding="utf-8") as file:
            data = json.load(file)
        for theme, liste_questions in data.items():
            self.questions_par_theme[theme] = [
                Questions(
                    q["question"],
                    q["reponses"],
                    q["bonne_reponse"],
                    categorie=theme
                ) for q in liste_questions
            ]

    def determiner_premier_joueur(self):
        """Détermine le premier joueur (le plus jeune)."""
        premier_joueur = min(self.joueurs, key=lambda joueur: joueur.age)
        print(f"\n{premier_joueur.nom} commence le jeu !")
        self.tour_actuel = self.joueurs.index(premier_joueur)

    def lancer_manche(self):
        """Exécute une manche du jeu."""
        joueur = self.joueurs[self.tour_actuel]
        print(f"\nC'est au tour de {joueur.nom} !")

        # Lancer le dé
        resultat = joueur.lancer_de()
        print(f"{joueur.nom} a lancé le dé et a obtenu : {resultat}")

        # Déplacer le joueur
        joueur.position = (joueur.position + resultat) % self.plateau.nombre_cases
        case = self.plateau.obtenir_case(joueur.position)
        print(f"{joueur.nom} se trouve maintenant sur la {case}.")

        # Poser une question
        questions = self.questions_par_theme.get(case.couleur, [])
        if questions:
            question = random.choice(questions)
            if question.poser():
                print("Bonne réponse ! 🎉")
                if  case.couleur not in joueur.camemberts:
                    joueur.ajouter_camembert(case.couleur)

                    # Vérifier si le joueur a gagné
                    if joueur.a_tous_les_camemberts():
                        print(f"\nFélicitations {joueur.nom}, vous avez gagné le jeu ! 🎉")
                        return True

                # Si bonne réponse, rejouer
                print(f"{joueur.nom} rejoue !")
                return False  # Le joueur continue de jouer

            else:
                print("Mauvaise réponse 😞.")

        # Passer au joueur suivant
        self.tour_actuel = (self.tour_actuel + 1) % len(self.joueurs)
        return False

    def lancer_jeu(self):
        """Lance le jeu complet."""
        print("Bienvenue dans le jeu !")
        self.initialiser_joueurs()
        self.charger_questions("/questions_trivial_pursuit.json")
        self.determiner_premier_joueur()
        while not self.lancer_manche():
          pass


# Lancer le jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancer_jeu()

