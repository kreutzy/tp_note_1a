from petale import Petale
from fleur import Fleur
from feuille import Feuille
from random import random, randint

class Branche:
    """[summary]
    Attributs
    ---------
    epaisseur: float
    angle: float
    liste_branches_filles : liste
    liste_fleurs : liste
    liste_feuilles: liste
    
    
    """    
    def __init__(self):
        """[Constructeur de branche]
        """        
        self.epaisseur = 5
        self.liste_branches_filles=[]
        self.liste_fleurs=[]
        self.liste_feuilles=[Feuille()]
        self.angle = randint()
    
    def nb_branches(self):
        pass
    def nb_feuilles(self):
        pass
    def nb_fleurs(self):
        pass
    def nb_fruits(self):
        pass
    def vieillir(self, saison):
        pass
    def couleur(self):
        pass            
        