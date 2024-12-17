class Jeu:
    def __init__(self):
        self.joueurs = []
        self.questions_par_theme = {}
        self.tour_actuel = 0
        self.manche = 1

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
        """Détermine le premier joueur en fonction de l'âge le plus jeune."""
        premier_joueur = min(self.joueurs, key=lambda joueur: joueur.age)
        print(f"\n{premier_joueur.nom} commence le jeu !")
        self.tour_actuel = self.joueurs.index(premier_joueur)

    def joueur_suivant(self):
        """Passe au joueur suivant."""
        self.tour_actuel = (self.tour_actuel + 1) % len(self.joueurs)
        return self.joueurs[self.tour_actuel]

    def lancer_manche(self):
        """Exécute une manche du jeu."""
        joueur = self.joueurs[self.tour_actuel]
        print(f"\n--- Manche {self.manche} ---")
        print(f"C'est au tour de {joueur.nom} !")

        # Lancer le dé
        resultat = joueur.lancer_de()
        print(f"{joueur.nom} a lancé le dé et a obtenu : {resultat}")

        # Déplacer le joueur
        self.se_deplacer(joueur, resultat)

        # Déterminer et poser une question
        case = self.determiner_case(joueur.position)
        self.poser_question(case, joueur)

        # Vérifier la condition de victoire
        if joueur.a_tous_les_camemberts():
            print(f"\nFélicitations {joueur.nom} ! Vous avez gagné le jeu 🎉 !")
            return True

        self.tour_actuel = (self.tour_actuel + 1) % len(self.joueurs)
        self.manche += 1
        return False

    def se_deplacer(self, joueur, resultat):
        """Déplace le joueur sur le plateau."""
        ## joueur.position = (joueur.position + resultat) % 40
        print(f"{joueur.nom} se déplace à la case {joueur.position}.")

    def determiner_case(self, position):
        """Détermine la case où se trouve le joueur."""
        couleurs = ["Bleu", "Rose", "Jaune", "Vert", "Orange", "Violet"]
        couleur = couleurs[position % len(couleurs)]
        return Case(couleur, "Général")  # Les catégories peuvent évoluer

    def poser_question(self, case, joueur):
        """Pose une question basée sur la case."""
        questions = self.questions_par_theme.get(case.couleur, [])
        if questions:
            question = random.choice(questions)
            if question.poser():
                print("Bonne réponse ! 🎉")
                joueur.ajouter_camembert(case.couleur)
            else:
                print("Mauvaise réponse 😞.")

    for theme, questions in jeu.questions_par_theme.items():
        print(f"\nThème : {theme}")
        for question_data in questions:
            question = Question(
                texte=question_data["question"],
                reponses=question_data["reponses"],
                bonne_reponse_index=question_data["bonne_reponse_index"],
                categorie=theme
            )
            question.poser()

        time.sleep(1)  # Pause pour un meilleur rythme de jeu
