"""
Nom du fichier : exemple.py
Description : Ce fichier contient un exemple de bonnes pratiques en Python.
Auteur : Votre Nom
Date : 10 septembre 2024
"""

import sys

def mots_Nlettres(lstMot:list, char:str)->list:
    lstWordWithChar = []
    for elt in lstMot :
        if char in elt :
            lstWordWithChar.append(elt)
            
    return lstWordWithChar



def test_exo2(lstSend: list)->None:
    print(mots_Nlettres(lstSend,""))


def main():
    """ Point d'entrée du programme."""
    
    lstWord = ["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"]
    
    test_exo2(lstWord)
    
    


if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")