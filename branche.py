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
        self.angle = random(-90,90)
    
    def nb_branches(self):
        return len(self.liste_branches_filles)
    
    
    
    
    def nb_feuilles(self):
        
        compteur_feuilles = len(self.liste_feuilles)
        
        if compteur_feuilles>0:
            return compteur_feuilles
        else:
            for branche in self.liste_branches_filles:
                compteur_feuilles += branche.nb_feuilles()    
            return compteur_feuilles   
        
    def nb_fleurs(self):
        compteur_fleurs = 0
        for fleur in self.liste_fleurs:
            if not fleur.est_fruit():
                compteur_fleurs +=1
        if compteur_fleurs > 0:
            return compteur_fleurs
        else:
            for branche in self.liste_branches_filles:
                compteur_fleurs += branche.nb_fleurs()
            return compteur_fleurs
        
    def nb_fruits(self):
        compteur_fruit = 0
        for fleur in self.liste_fleurs:
            if fleur.est_fruit():
                compteur_fruit += 1
        if compteur_fruit > 0:
            return compteur_fruit
        else:
            for branche in self.liste_branches_filles:
                compteur_fruit += branche.nb_fruits()
            return compteur_fruit
             
    def vieillir_branche(self, saison):
        #probabilité que la branche casse
        if random() < 0.1/self.epaisseur :
            return (False, self.nb_fruits())
        self.epaisseur += 0.015 # la branche vieillit chaque jour, donc à chaque appel de la méthode
        
        #les feuilles vieillissent et peuvent tomber
        for feuille in self.liste_feuilles:
            esttombee = feuille.vieillir(saison)
            if esttombee:
                self.liste_feuilles.remove(feuille)
        
        #les fleurs vieillissent
        compteur_fruits_tombes = 0
        for fleur in self.liste_fleurs:
            condition_fruit_tombe = [fleur.vieillir(), fleur.est_fruit()]
            if condition_fruit_tombe == [True, True]:
                compteur_fruits_tombes +=1
                self.liste_fleurs.remove(fleur)
        
        for branche_fille in self.liste_branches_filles:
        
        
        if saison==1:
            if self.liste_fleurs == []:
                if self.liste_feuilles == []:
                    if self.liste_branches_filles == []:
                        nombre_nouvelles_branches = randint(1,5)
                    
                
        
        
    def couleur(self):
        pass            
        