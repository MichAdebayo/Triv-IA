import random
import time

class Joueur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.camemberts = set()
        self.score = 0        
        self.position = 0

    def ajouter_camembert(self, couleur):
        self.camemberts.add(couleur)
        print(f"{self.nom} a gagné un camembert de couleur {couleur} !")

    def a_tous_les_camemberts(self):
      return len(self.camemberts) == 6

    def lancer_de(self):
      return random.randint(1, 6)

class Jeu:
    def __init__(self):
        self.joueurs = []
        self.manche = 1
        self.tour_actuel = 0

    def initialiser_joueurs(self):
        nb_joueurs = int(input("Entrez le nombre de joueurs (entre 2 et 6) : "))
        while nb_joueurs < 2 or nb_joueurs > 6:
            nb_joueurs = int(input("Entrez un nombre de joueurs valide (entre 2 et 6) : "))

        for i in range(nb_joueurs):
            nom = input(f"Entrez le nom du joueur {i + 1} : ")
            self.joueurs.append(Joueur(nom))

    def determiner_premier_joueur(self):
          premier_joueur = min(self.joueur, key=age.get)
          print(f"{premier_joueur.nom} commence le jeu !")
          self.tour_actuel = self.joueurs.index(premier_joueur)

    def joueur_suivant(self):
        self.tour_actuel = (self.tour_actuel + 1) % len(self.joueurs)
        return self.joueurs[self.tour_actuel]

    def lancer_manche(self):
        print(f"\n--- Manche {self.manche} ---")
        joueur = self.joueurs[self.tour_actuel]
        print(f"C'est au tour de {joueur.nom} !")

        resultat = joueur.lancer_de()
        print(f"{joueur.nom} a lancé le dé et a obtenu : {resultat}")
        self.se_deplacer(joueur, resultat)

        case = self.determiner_case(joueur.position)
        self.poser_question(case, joueur)

        if joueur.a_tous_les_camemberts():
            print(f"\n{joueur.nom} a gagné le jeu !")
            return True

        self.manche += 1
        return False


    def se_deplacer(self, joueur, resultat):
        joueur.position = (joueur.position + resultat) % 40
        print(f"{joueur.nom} se déplace à la case {joueur.position}.")

    def poser_question(self, case, joueur):
            questions = questions_trivial_pursuit.get(case.couleur, [])
            if questions:
                question_data = random.choice(questions)
                # Créer une instance de Question avec les données du JSON
                question = Question(
                    texte=question_data["question"],
                    reponses=question_data["reponses"],
                    bonne_reponse=question_data["bonne_reponse"],
                    categorie=case.couleur
                )
                if question.poser():
                    print("Bonne réponse !")
                    joueur.ajouter_camembert(case.couleur)
                else:
                    print("Mauvaise réponse.")

        
        # Vérifier si le joueur a gagné
        if joueur.a_tous_les_camemberts():
            print(f"\n{joueur.nom} a gagné le jeu !")
            return True  # Fin du jeu

        # Passer au joueur suivant
        self.tour_actuel = (self.tour_actuel + 1) % len(self.joueurs)
        self.manche += 1
        return False  # Le jeu continue



    def se_deplacer(self, joueur, resultat):
        nouvelle_position = (joueur.position + resultat) % 40
        joueur.position = nouvelle_position

    def charger_questions(self, fichier_json):
        with open(fichier_json, "r", encoding="utf-8") as file:
            data = json.load(questions_trivial_pursuit.json)
        questions_par_theme = {}

        # Convertir les données JSON en objets Question
        for theme, liste_questions in data.items():
            questions_par_theme[theme] = [
                Question(q["question"], q["reponses"], q["bonne_reponse"])
                for q in liste_questions
            ]
        return questions_par_theme

class Questions:
   def __init__(self, question, reponses, bonne_reponse_index, categorie):
        self.question = question
        self.reponses = reponses
        self.bonne_reponse = reponses[bonne_reponse_index]
        self.categorie = categorie
      
    def poser(self):
        print(f"Question ({self.categorie}): {self.question}")
        for i, reponse in enumerate(self.reponses, 1):
            print(f"{i}. {reponse}")
        choix = input("Votre réponse (numéro) : ")
        reponse = int(choix) - 1 == self.bonne_reponse_index
        return reponse


class Case:
    def __init__(self, couleur, categorie):
        self.couleur = couleur
        self.categorie = categorie
    #### .....




# Lancer le jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.initialiser_joueurs()
    jeu.determiner_premier_joueur()
    if joueur[cammenbert] = 6
      print("Fin du jeu")
    else:
      jeu.lancer_manche()
      jeu.poser_question()
