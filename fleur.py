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
        """[Constructeur de la fleur]
        Construit une fleur avec 10 pétales
        """        
        self.age=0
        self.fecondee = False
        self.liste_petales=[]
        for i in range(10):
            self.liste_petales.append(Petale())
        


    def est_fanant(self):
        """[indique si la fleur est en train de fâner]

        Returns:
            [bool]: [True si la fleur fane, False sinon]
        """        
        if self.age >15 and self.age < 21:
            return True
        else:
            return False

    def est_fruit(self):
        """[indique si la fleur est en fruit]

        Returns:
            [bool]: [True si la fleur est en fruit, False sinon]
        """        
        if self.age > 20 and self.age <31 and (self.fecondee==True):
            return True
        else:
            return False

    def vieillir(self):
        """[Fait vieillir la fleur]
        
        Returns
        -------
        bool:
            True si la fleur/fruit est tombé(e)
        """        
        self.age += 1 # la fleur prend un jour
        # on fait vieillir chaque pétale
        for petale in self.liste_petales:
            petale.vieillir()
        #probabilité d'être butinée (donc fécondée)
        if self.age <16:
            if random() < 0.08:
                self.fecondee = True
        # probabilité de tomber de l'arbre
        if random < 0.01:
            self.age=31
        if self.age >=31:
            return True 
        else:
            return False
        

    def couleur(self):
        """[indique la couleur de la fleur selon son état de fleur ou de fruit]

        Returns:
            [dict]: [dictionnaire comprenant, si la fleur n'est pas un fruit, la valeur du "coeur_jaune" et la valeur
            de la "couleur_des_petales", sinon (la fleur est un fruit) comprend uniquement la valeur 1 pour la couleur orange]
        """        
        dictionnaire_couleurs = {}
        if self.est_fruit():
            dictionnaire_couleurs["orange"] = 1
        else:

            nombre_petales = 0
            for petale in self.liste_petales:
                if petale.age <21:
                    nombre_petales +=1
            
            dictionnaire_couleurs["coeur_jaune"] = 1/(1+nombre_petales)
            dictionnaire_couleurs["couleur_des_petales"] = nombre_petales/(1+nombre_petales)

        return print(dictionnaire_couleurs)
