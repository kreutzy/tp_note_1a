from petale import Petale
from fleur import Fleur
from feuille import Feuille
from branche import Branche
from random import random

class Arbre(Branche):
    """[summary]
    """    
    def __init__(self):
        super().__init__(self)
        self.coordonnees = (random(), random())
        
