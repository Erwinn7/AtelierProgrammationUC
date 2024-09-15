"""
Nom du fichier : exemple.py
Description : Ce fichier contient un exemple de bonnes pratiques en Python.
Auteur : Votre Nom
Date : 10 septembre 2024
"""

import sys


def somme_recursive(lstNumbre:list[float])->float:
    """return a sum of number in the list 

    Args:
        lstNumbre (list[float]): list of float number 

    Returns:
        float: sum of list's numbers
    """
    result = 0
    if len(lstNumbre) != 0:
        result = lstNumbre[0] + somme_recursive(lstNumbre[1:])

    return result
    
    
    
def factorielle_recursive(number:int)->int:
    """_summary_

    Args:
        number (int): _description_

    Returns:
        int: _description_
    """
    result = 1
    if number > 1 :
        result = number * factorielle_recursive(number - 1)
        
    return result


def longueur(lstElts:list)->int:
    """return lenght of listElts
 
    Args:
        lstElts (list): list of elements

    Returns:
        int: list's length
    """
    result = 0
    if lstElts :
        result = 1 + longueur(lstElts[1:])
        
    return result
    

def minimum(lstElts:list)->int:
    """_summary_

    Args:
        lstElts (list): _description_

    Returns:
        int: _description_
    """
    result = 0 
    if lstElts :
        element = 0
        if len(lstElts) == 1:
            result = lstElts[0]
        elif len(lstElts) > 1 and lstElts[-1] > lstElts[0] : 
            element = lstElts[-1]
            lstElts.remove(element)
            minimum(lstElts)
        elif len(lstElts) > 1 and  lstElts[-1] <  lstElts[0] :
            element = lstElts[0]
            lstElts.remove(element)
            minimum(lstElts)
    
    return result


def main():
    """ Point d'entrée du programme."""
    
    # Test de la fonction
    # liste1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    # resultat1 = somme_recursive(liste1)
    # print("La somme de la liste est :", resultat1)
    # liste2 = []
    # resultat2 = somme_recursive(liste2)
    # print("La somme de la liste est :", resultat2)


    # Test de la fonction
    # nombre = 5
    # resultat = factorielle_recursive(nombre)
    # print("Le factoriel de", nombre, "est :", resultat)
    
    
    # Test de la fonction
    liste1 = [1, 2, 3, 4, 5]
    resultat1 = minimum(liste1)
    print("La somme de la liste est :", resultat1)
    liste2 = []
    resultat2 = minimum(liste2)
    print("La somme de la liste est :", resultat2)
   

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")