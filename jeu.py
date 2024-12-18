from plateau import Plateau
import random
import json

class Jeu:
    def __init__(self):
        self.joueurs = []
        self.tour_actuel = 0
        self.plateau = Plateau()

    def initialiser_joueurs(self):
        nb_joueurs = input('\n Veuillez saisir un nombre de joueur(max 6 joueurs)   ')

        animaux = [
            "🐱",  # Chat
            "🐶",  # Chien
            "🐻",  # Ours
            "🐸",  # Grenouille
            "🐯",  # Tigre
            "🐧"   # Pingouin
        ]


        for i in range(int(nb_joueurs)):

            nb_joueurs = input('\n Veuillez saisir un nombre de joueur(max 6 joueurs)   ')

            animaux = [
                "🐱",  # Chat
                "🐶",  # Chien
                "🐻",  # Ours
                "🐸",  # Grenouille
                "🐯",  # Tigre
                "🐧"   # Pingouin
            ]


            for i in range(int(nb_joueurs)):

                nom_du_joueur = input('saisissez le nom du joueur   ')


                emoji_joueur = random.choice(animaux)
                animaux.remove(emoji_joueur)
                print(f"vous êtes l'emoji {emoji_joueur}")
                self.joueurs.append([nom_du_joueur, emoji_joueur])

    # def determiner_premier_joueur(self):
    #     """Détermine le premier joueur (le plus jeune)."""
    #     premier_joueur = min(self.joueurs, key=lambda joueur: joueur.age)
    #     print(f"\n{premier_joueur.nom} commence le jeu !")
    #     self.tour_actuel = self.joueurs.index(premier_joueur)

    def lancer_manche(self):
        """Exécute une manche du jeu."""
        joueur = self.joueurs[self.tour_actuel]
        print(f"\nC'est au tour de {joueur.nom} !")

        # Lancer le dé
        resultat = joueur.lancer_de()
        print(f"{joueur.nom} a lancé le dé et a obtenu : {resultat}")

        # Déplacer le joueur

        case = self.plateau.obtenir_case(joueur.position)
        choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')
        if choix_mouvement != 'ar' or choix_mouvement != 'av':
            choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')

        if choix_mouvement == 'av':
            joueur.position += resultat
        else:
            choix_mouvement == 'ar'
            joueur.position -= resultat

        joueur.position = joueur.position % len(self.plateau.cases)


            
        print(f"{joueur.nom} se trouve maintenant sur une case {self.plateau.cases[joueur.position].categorie}.")

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

    def poser(case_joueur):
        """Pose la question au joueur et retourne s'il a répondu correctement."""
        with open('questions_trivial_pursuit.json', 'r') as files:
            question = json.load(files)

        cat_question = case_joueur.categorie
        question_posee = random.choice(question[cat_question])

        print(f"\nQuestion ({cat_question}): {question_posee['question']}")
        for i, reponse in enumerate(question_posee['reponses'], 1):
            print(f"{i}. {reponse}")

        choix = input("Votre réponse (numéro) : ")
        while not choix.isdigit() or not (1 <= int(choix) <= 4):
            print("Entrée invalide. Réessayez.")
            choix = input("Votre réponse (numéro) : ")

        return int(choix) - 1 == question_posee['bonne_reponse']  




    def lancer_jeu(self):
        """Lance le jeu complet."""
        print("Bienvenue dans le jeu !")
        self.initialiser_joueurs()
        self.charger_questions("/questions_trivial_pursuit.json")
        self.determiner_premier_joueur()
        while not self.lancer_manche():
          pass