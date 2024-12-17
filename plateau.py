
from case import Case
import random

class Plateau:
    def __init__(self, joueurs, cases):
        self.joueurs = []
        self.cases = []

    def creation_liste_cases(self):
        types_possibles = ['Camembert', 'Normale']
        categories = ['Base de données', 'Python', 'Unix', 'Actu IA', 'Devops',"Personnalité de l'IA"]


        cat_cam = categories.copy()
        for i in range(1,37):
            if i == 1 or i % 6 == 1:
                cat_case = random.choice(cat_cam)
                cat_cam.remove(cat_case)
                new_case = Case(categorie= cat_case,position = i, type = types_possibles[0])
                self.liste_cases.append(new_case)
                cat = categories.copy()
                cat.remove(cat_case)


            else:
                cat_case_normale = random.choice(cat)
                cat.remove(cat_case_normale)
                new_case = Case(categorie= cat_case_normale,position = i, type = types_possibles[1])
                self.liste_cases.append(new_case)

                


    def creer_plateau(self):

        types_possibles = ['Camembert', 'Normale']
        categories = ['Base de données', 'Python', 'Unix', 'Actu IA', 'Devops',"Personnalité de l'IA"]
        emojis = [
            "🟦",  # Carré bleu
            "🟩",  # Carré vert
            "🟥",  # Carré rouge
            "🟨",  # Carré jaune
            "🟧",  # Carré orange
            "🟪",  # Carré violet
        ]

        emojis_ronds = [
            "🔵",  # Cercle bleu
            "🟢",  # Cercle vert
            "🔴",  # Cercle rouge
            "🟡",  # Cercle jaune
            "🟠",  # Cercle orange
            "🟣",  # Cercle violet
        ]

        for i in range(1,13):

            if i < 13:
                if self.liste_cases[i-1].categorie == categories[0]:
                    print(emojis[0], end = '   ')

                if self.liste_cases[i-1].categorie == categories[1]:
                    print(emojis[1], end = '   ')

                if self.liste_cases[i-1].categorie == categories[2]:
                    print(emojis[2], end = '   ')

                if self.liste_cases[i-1].categorie == categories[3]:
                    print(emojis[3], end = '   ')

                if self.liste_cases[i-1].categorie == categories[4]:
                    print(emojis[4], end = '   ')

                if self.liste_cases[i-1].categorie == categories[5]:
                    print(emojis[5], end = '   ')

        print('\n')


        c = 36
        c1 = 13
        while c >= 31:
            if self.liste_cases[c-1].categorie == categories[0]:
                print(emojis[0], end = '   ')

            if self.liste_cases[c-1].categorie == categories[1]:
                print(emojis[1], end = '   ')

            if self.liste_cases[c-1].categorie == categories[2]:
                print(emojis[2], end = '   ')

            if self.liste_cases[c-1].categorie == categories[3]:
                print(emojis[3], end = '   ')

            if self.liste_cases[c-1].categorie == categories[4]:
                print(emojis[4], end = '   ')

            if self.liste_cases[c-1].categorie == categories[5]:
                print(emojis[5], end = '   ')

            print(' '* 48, end = '   ')

            if self.liste_cases[c1-1].categorie == categories[0]:
                print(emojis[0], end='\n\n')

            if self.liste_cases[c1-1].categorie == categories[1]:
                print(emojis[1], end='\n\n')

            if self.liste_cases[c1-1].categorie == categories[2]:
                print(emojis[2], end='\n\n')

            if self.liste_cases[c1-1].categorie == categories[3]:
                print(emojis[3], end='\n\n')

            if self.liste_cases[c1-1].categorie == categories[4]:
                print(emojis[4], end='\n\n')

            if self.liste_cases[c1-1].categorie == categories[5]:
                print(emojis[5], end='\n\n')
            c -= 1
            c1 +=1
        for i in range(30, 18, -1):
            if self.liste_cases[i-1].categorie == categories[0]:
                print(emojis[0], end= '   ')

            if self.liste_cases[i-1].categorie == categories[1]:
                print(emojis[1], end = '   ')

            if self.liste_cases[i-1].categorie == categories[2]:
                print(emojis[2], end = '   ')

            if self.liste_cases[i-1].categorie == categories[3]:
                print(emojis[3], end = '   ')

            if self.liste_cases[i-1].categorie == categories[4]:
                print(emojis[4], end = '   ')

            if self.liste_cases[i-1].categorie == categories[5]:
                print(emojis[5], end = '   ')



    def get_case(self, i):
        self.cases[i]

    