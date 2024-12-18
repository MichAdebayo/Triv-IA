
from case import Case
import random


class Plateau:
    

    def __init__(self, joueurs= [], cases=[]):
        self.joueurs = joueurs
        self.cases = cases


    def creation_cases(self):
        types_possibles = ['Camembert', 'Normale']
        categories = ['Base de données', 'Python', 'Unix', 'Actu IA', 'Devops',"Personnalité de l'IA"]


        cat_cam = categories.copy()
        for i in range(1,37):
            if i == 1 or i % 6 == 1:
                cat_case = random.choice(cat_cam)
                cat_cam.remove(cat_case)
                new_case = Case(categorie= cat_case,position = i, type = types_possibles[0])
                self.cases.append(new_case)
                cat = categories.copy()
                cat.remove(cat_case)


            else:
                cat_case_normale = random.choice(cat)
                cat.remove(cat_case_normale)
                new_case = Case(categorie= cat_case_normale,position = i, type = types_possibles[1])
                self.cases.append(new_case)



    def creation_joueur(self):

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

            age_joueur = input(f"quel est l'age de {nom_du_joueur} ?    ")

            emoji_joueur = random.choice(animaux)
            animaux.remove(emoji_joueur)
            print(f"vous êtes l'emoji {emoji_joueur}")
            self.joueurs.append([nom_du_joueur, age_joueur, emoji_joueur])


    def deplacement_joueur(self,i):
        lancer = self.joueurs[i].lancer_de()
        choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')
        if choix_mouvement != 'ar' or choix_mouvement != 'av':
            choix_mouvement = input('Si vous voulez aller en avant tapez av pour aller en arriere tapez ar ')

        if choix_mouvement == 'av':
            self.joueurs[i].position += lancer
        else:
            choix_mouvement == 'ar'
            self.joueurs[i].position -= lancer


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
            

            
            if self.cases[i-1].categorie == categories[0]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[0], end = '    ')
                else:
                    print(emojis[0], end = '   ')

            elif self.cases[i-1].categorie == categories[1]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[1], end = '    ')
                else:
                    print(emojis[1], end = '   ')

            elif self.cases[i-1].categorie == categories[2]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[2], end = '    ')
                else:
                    print(emojis[2], end = '   ')

            elif self.cases[i-1].categorie == categories[3]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[3], end = '    ')
                else:
                    print(emojis[3], end = '   ')

            elif self.cases[i-1].categorie == categories[4]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[4], end = '    ')
                else:
                    print(emojis[4], end = '  ')

            elif self.cases[i-1].categorie == categories[5]:
                if self.cases[i-1].type == types_possibles[0]:
                    print(emojis_ronds[5], end = '    ')
                else:
                    print(emojis[5], end = '   ')
                    
        print('\n')


        c = 36
        c1 = 13
        while c >= 31:
            if self.cases[c-1].categorie == categories[0]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[0], end = '    ')
                else:
                    print(emojis[0], end = '   ')

            elif self.cases[c-1].categorie == categories[1]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[1], end = '    ')
                else:
                    print(emojis[1], end = '   ')

            elif self.cases[c-1].categorie == categories[2]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[2], end = '    ')
                else:
                    print(emojis[2], end = '   ')

            elif self.cases[c-1].categorie == categories[3]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[3], end = '    ')
                else:
                    print(emojis[3], end = '   ')

            elif self.cases[c-1].categorie == categories[4]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[4], end = '   ')
                else:
                    print(emojis[4], end = '   ')

            elif self.cases[c-1].categorie == categories[5]:
                if self.cases[c-1].type == types_possibles[0]:
                    print(emojis_ronds[5], end = '    ')
                else:
                    print(emojis[5], end = '   ')
                    
            print(' '* 49, end = '   ')

            if self.cases[c1-1].categorie == categories[0]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[0], end='\n\n')
                else:
                    print(emojis[0], end='\n\n')

            elif self.cases[c1-1].categorie == categories[1]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[1], end='\n\n')
                else:
                    print(emojis[1], end='\n\n')

            elif self.cases[c1-1].categorie == categories[2]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[2], end='\n\n')
                else:
                    print(emojis[2], end='\n\n')

            elif self.cases[c1-1].categorie == categories[3]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[3], end='\n\n')
                else:
                    print(emojis[3], end='\n\n')

            elif self.cases[c1-1].categorie == categories[4]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[4], end='\n\n')
                else:
                    print(emojis[4], end='\n\n')

            elif self.cases[c1-1].categorie == categories[5]:
                if self.cases[c1-1].type == types_possibles[0]:       
                    print(emojis_ronds[5], end='\n\n')
                else:
                    print(emojis[5], end='\n\n')

            c -= 1
            c1 +=1


        for i in range(30, 18, -1):
                
                if self.cases[i-1].categorie == categories[0]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[0], end = '    ')
                    else:
                        print(emojis[0], end = '   ')

                elif self.cases[i-1].categorie == categories[1]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[1], end = '    ')
                    else:
                        print(emojis[1], end = '   ')

                elif self.cases[i-1].categorie == categories[2]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[2], end = '    ')
                    else:
                        print(emojis[2], end = '   ')

                elif self.cases[i-1].categorie == categories[3]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[3], end = '    ')
                    else:
                        print(emojis[3], end = '   ')

                elif self.cases[i-1].categorie == categories[4]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[4], end = '    ')
                    else:
                        print(emojis[4], end = '   ')

                elif self.cases[i-1].categorie == categories[5]:
                    if self.cases[i-1].type == types_possibles[0]:
                        print(emojis_ronds[5], end = '    ')
                    else:
                        print(emojis[5], end = '   ')





    def get_case(self, i):
        self.cases[i]


if __name__ == '__main__':
    partie = Plateau()

    partie.creation_cases()
    partie.creer_plateau()
    partie.creation_joueur()
    print(partie.joueurs)


    