import numpy as np
import matplotlib.pyplot as plt
#Solal Martin
#Version impérative

def showPuissance4(mat):
    plt.figure(figsize=(7, 6))
    plt.grid(True, color='blue', linestyle='-')
    ax = plt.gca()
    ax.set_xlim([0, 7])
    ax.set_ylim([0, 6])
    for x in range(0, len(mat)):
        for y in range(0, len(mat[x])):
            if mat[x][y] == 1:
                plt.scatter(x + 0.5, y + 0.5, color='r', s=1300)
            elif mat[x][y] == 2:
                plt.scatter(x + 0.5, y + 0.5, color='y', s=1300)
    plt.show()


def Init():
    t = np.zeros(42)
    m = t.reshape(7, 6) #on inverse ligne et colonne afin que notre matrice ait les bonnes dimensions avec le showpuissance
    return m


m1 = Init()

def Position(m, col, coul):
    l = [] #on crée une liste afin de positionner notre pion à la première place vide de notre colonne
    for i in range(0, m.shape[1]):
        if m[col, i] == 0:
            l += [i]
    m[col, l[0]] = coul #l[0] représente bien la première place vide de la colonne
    return m

def Victoire(m, pions):
    #on fait une double itération sur les colonnes puis les lignes de la matrice ou inversement, c'est pour cela qu'on prend 7 et 6 car cela répresente le nb de ligne et de colonnes dans notre matrice
    for j in range(0, 3): #on s'arrête à 3 pour ne pas sortir de la matrice
        for i in range(0, 7):
            if m[i][j] == pions and m[i][j + 1] == pions and m[i][j + 2] == pions and m[i][j + 3] == pions:

                return "Victoire en colonnes" #verifie si le joueur gagne verticalement


    for i in range(0,4):
        for j in range(0, 6):
            if m[i][j] == pions and m[i + 1][j] == pions and m[i + 2][j] == pions and m[i + 3][j] == pions:

                return "Victoire en lignes" #verifie si le joueur gagne horizontalement


    for i in range(0, 4):
        for j in range(0,3):
            if m[i][j] == pions and m[i + 1][j + 1] == pions and m[i + 2][j + 2] == pions and m[i + 3][j + 3] == pions:

                return "Victoire en diag 1" #verifie si le joueur gagne avec une diagonale montante
    for j in range(0, 3):
        for i in range(3, 7):
            if m[i][j] == pions and m[i - 1][j + 1] == pions and m[i - 2][j + 2] == pions and m[i - 3][j + 3] == pions:

                return "Victoire en diag 2" #verifie si le joueur gagne avec une diagonale descendante


def Partiejeu(m):

    while Victoire(m,1)==None and Victoire(m,2)==None and len(np.where(m==0)[1])>0 : #boucle tant que ni 1 ni 2 ont gagné et qu'il reste des 0 (de la place) dans la matrice
        c = int(input("Joueur 1 choisissez une colonne"))
        m = Position(m, c, 1)
        if Victoire(m, 1) == None:
            d = int(input("joueur 2 choississez une colonne"))
            m = Position(m, d, 2)

        showPuissance4(m)

    if Victoire(m,1)!=None:
        print("Félicitations joueur 1 vous avez gagné")
        return showPuissance4(m)
    elif Victoire(m,2)!=None :
        print("Félicitations joueur 2 vous avez gagné")
        return showPuissance4(m)
    else :
        print("Match Nul")
        return showPuissance4(m)

#Partie Orientée objet
class Puissance4:
    def __init__(self,matrice, entier):
        self.matrice=matrice
        self.joueur_courant=entier
    def tour(self,col):

        self.matrice=Position(self.matrice,col,self.joueur_courant)
        return self.matrice

    def victoire(self,m):
        if Victoire(m,self.joueur_courant) != None:
           return True

    def boucle_de_jeu(self):
       prenom1=input("joueur 1, rentrez votre prénom")
       prenom2=input("joueur 2, rentrez votre prénom")
       gagnant=False
       while gagnant == False and len(np.where(self.matrice==0)[1])>0 : #même principe que pour la version impérative
           self.joueur_courant=1
           c=int(input(prenom1 + " Choississez une colonne entre 0 et 6"))
           if self.victoire(self.tour(c))!=True:
               self.joueur_courant=2
               d = int(input(prenom2 + " Choississez une colonne entre 0 et 6 "))

               if self.victoire(self.tour(d)) == True:
                   gagnant=True
                   print(prenom2 + " a gagné")


           else:
               gagnant=True
               print(prenom1 + " a gagné")
           showPuissance4(self.matrice)
       if gagnant == False:
           print("Match Nul")

       return showPuissance4(self.matrice)

P=Puissance4(Init(),1)
P.boucle_de_jeu()






