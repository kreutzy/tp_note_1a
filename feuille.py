from petale import Petale
from fleur import Fleur
from random import random

class Feuille:
    """[summary]
      Attributes
    ----------
    sechant: int
        indique  le nombre de jours passé par la feuille à sécher à l'automne (quand
        elle change de couleur). Après 10 jours, la feuille tombe


    Parameters
    ----------
    """    
    def __init__(self):
        """[Constructeur de Feuille]
            Initialise le nombre de jours passés à sécher à 0
            Après 10 jours de séchage, la feuille tombe. 
        
        Examples
        --------
        """        
        self.sechant = 0
    
    def statut(self):
        """[renvoie l'état de la feuille]

        Returns:
            [str]: [retourne 'vivante' ou 'séchante' selon l'état de la feuille]
        
        Examples
        --------
        >>> maFeuille = Feuille()
        >>> maFeuille.sechant==0
        True
        """ 
        # Attention, l'appel à la méthode vieillir peut incrémenter séchant
        sechant_actuel = self.sechant
        resultat_vieillir = self.vieillir(0)
        # remise à l'état de l'attribut séchant en cas de vieillissement "prématuré"
        if self.sechant != sechant_actuel:
            self.sechant -= 1
        # si la feuille n'a pas commencé à sécher et n'est pas tombée
        if self.sechant == 0 and resultat_vieillir == False:
            return 'vivante'
        else:
            return 'séchante'


    def vieillir(self, saison):
        """[Fait vieillir la feuille selon la saison et un aléa]

        Args:
            saison ([int]): [vaut 0, 1, 2 ou 3 selon la saison en cours]

        Returns:
            [bool]: [vaut True si la feuille est tombée]
        Examples
        --------
        >>> maFeuille = Feuille()
        >>> maFeuille.vieillir(0)
        False
        >>> maFeuille.sechant
        1
        """        
        est_tombee = False
        if random() <0.0005:
            est_tombee = True
        if saison == 0: # En hiver
            self.sechant += 1
        if saison == 3: # en automne
            if random() < 0.05:
                self.sechant +=1
        if self.sechant >10:
            est_tombee = True
        return est_tombee

    def couleur(self):
        """[renvoie la couleur de la feuille selon le statut ]
        
        Examples
        --------
        >>> maFeuille = Feuille()
        >>> maFeuille.couleur()

        
        """        
        if self.statut() == 'vivante':
            return 'vert'
        elif self.sechant < 6:
            return 'jaune'
        else:
            return 'marron'
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()