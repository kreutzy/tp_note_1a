from petale import Petale
from random import random #aléatoire pour la méthode vieillir
# 2. [Classe Fleur] 
# Implémentez la classe Fleur, sans oublier la liste des pétales indiquée par l'association 
# entre Fleur et Petale de la Figure 1. Le statut de la fleur dépend de ses attributs:
# âge jusqu'à 15 jours : en fleur
# âge entre 16 et 20 jours : fanant
# âge entre 21 et 30 jours, et fécondée : fruit
# âge plus de 21 jours non fécondée, ou plus de 31 jours ; tombée
# a) [Attributs]    Les fleurs ont un âge et un statut fécondée ou non

class Fleur:
    ''' Fleur
    
    Attributes
    ----------
    age: int
        âge de la fleur
    fecondee: bool
        est vraie si la fleur est fécondée, faux sinon
    liste_petales: list[Petale]
        contient la liste des pétales de la fleur

        
    Parameters
    ----------
    
    '''

    def __init__(self):
        self.age=0
        self.fecondee = False
        self.liste_petales=[]
        for i in range(10):
            self.liste_petales.append(Petale())
        print(self.liste_petales)


    def est_fanant():
        if self.age >15 and self.age < 21:
            return True
        else:
            return False

    def est_fruit():
        if self.age > 20 and self.age <31 and (self.fecondee==True):
            return True
        else:
            return False

    def vieillir():
        self.age += 1 # la fleur prend un jour
        # on fait vieiilir chaque pétale
        for petale in liste_petales:
            petale.vieillir()
        #probabilité d'être butinée (donc fécondée)
        if self.age <16:
            if random() < 0.08:
                self.fecondee = True
        # probabilité de tomber de l'arbre
        if random < 0.01:
            self.age=31
        

    def couleur():
        pass
    shdcjhsbd