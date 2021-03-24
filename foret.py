from petale import Petale
from fleur import Fleur
from feuille import Feuille
from branche import Branche
from arbre import Arbre
from random import random

class Foret():
    """[classe Forêt]
    Attributs
    ---------
    saison:int
        les saisons vont (dans l'ordre) de 0=hiver à 3=automne
    jour_saison:int
        il y a 91 jours par saison
    nb_graines:int
        les graines viennent des fruits tombés l'année précédente, elles disparaissent au 16e jour du printemps
    liste_arbres:int
        nombre d'arbres en vie dans la forêt
    """    
    def __init__(self, nb_arbres, saison):
        """[Constructeur de forêt]

        Args:
            nb_arbres ([int]): [nombre d'arbres à la création de la forêt]
            saison ([int]): [saison de départ]
        """        
        liste_arbres=[]
        for i in range(nb_arbres):
            liste_arbres.append(Arbre())
        self.saison = saison
        
    
    def __add__(self,int):
        