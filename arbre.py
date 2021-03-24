from petale import Petale
from fleur import Fleur
from feuille import Feuille
from branche import Branche
from random import random

class Arbre(Branche):
    """[Constructeur d'arbre]
    Attributs:
    coordonnees: tuple
        tuple constitué de deux float entre 0 et 1 correspondant aux coordonnées
    angle:float
        décrit l'angle, entre -90 et +90
    """    
    def __init__(self):
        super().__init__()
        self.coordonnees = (random(), random())
        self.angle = 0
