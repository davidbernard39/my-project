import random
import math

def play(n, mise):
    """ Joue sur le numéro "n" avec la mise "mise" et
        retourne le montant gagné en fonction de la mise : 
        Retourne 3 fois la mise si le numéro misé est le bon
        Retourne la moitié de la mise si le numéro misé 
        a la même parité que le numéro tiré
        Retourne 0 sinon
    """
    if (isinstance(n, int) is False):
        raise TypeError("Nombre invalide")
    
    result = random.randrange(50)
    print("Résultat du tirage :", result)
    
    if n == result:
        return mise * 3
    elif (n % 2 == 0 and result % 2 == 0) or (n % 2 != 0 and result % 2 != 0):
        return math.ceil(mise * .5)
    else:
        return 0
    