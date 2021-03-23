class Petale():
    ''' Petale
    
    Attributes
    ----------
    age: int
        âge du pétale
        
    Parameters
    ----------
    
    '''
    def __init__(self):
        '''Création d'un pétale
        
        Parameters
        ----------
        
        '''
        self.age=0
        
    def vieillir(self):
        ''' Incrémente l'âge et teste si le pétale
        est toujours accroché
        
        Parameters
        ----------
        
        Returns
        -------
        bool
            True si le pétale est toujours accroché
            
        Examples
        --------
        >>> monpetale = Petale()
        >>> monpetale.vieillir()
        True
        '''
        estaccroche = True
        self.age += 1
        
        if self.age > 20:
            estaccroche = False
        return estaccroche
        
    def couleur(self):
        ''' Retourne 'rouge' pour un pétale non fané
        'marron' pour un pétale commençant à faner
        
        Parameters
        ----------
        
        Returns
        -------
        str
        'rouge' ou 'marron'
            
        Examples
        --------
        >>> monpetale = Petale()
        >>> monpetale.couleur()
        'rouge'
        '''
        couleur_non_fane = 'rouge'
        couleur_fane = 'marron'
        if self.age<15:
            return couleur_non_fane
        else:
            return couleur_fane
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()