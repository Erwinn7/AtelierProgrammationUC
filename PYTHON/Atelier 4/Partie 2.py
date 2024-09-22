"""
Nom du fichier : exemple.py
Description : Ce fichier contient un exemple de bonnes pratiques en Python.
Auteur : Votre Nom
Date : 20 septembre 2024
"""

import sys
import numpy as np



def my_searchsorted(table : object, element: int )-> int:
    """
    Trouve l'indice d'insertion d'une valeur dans un tableau trié par la gauche.

    Args:
        table: Un tableau numpy trié.
        element: La valeur à insérer.

    Returns:
        L'indice d'insertion.
    """

    left, right = 0, len(table)
    while left < right:
        index = (left + right) // 2
        if table[index] < element:
            left = index + 1
        else:
            right = index
    return left

def my_where(table : object, valeur : int )-> list:   
    """
    Trouve les indices des éléments d'une matrice égaux à une valeur donnée sans utiliser NumPy.

    Args:
        matrix: La matrice sous forme de liste de listes.
        valeur: La valeur à rechercher.

    Returns:
        Une liste de tuples contenant les indices (ligne, colonne) des éléments trouvés.
    """

    indices = []
    for i, ligne in enumerate(table):
        for j, element in enumerate(ligne):
            if element == valeur:
                indices.append((i, j))
    return indices





def main():
    #Exemple d’usage de la fct searchsorted
    # arr = np.array([5, 7, 8, 9])
    # x = my_searchsorted(arr, 6)
    # print(x) #2
    
    #Exemple d’usage de la fct where sur une liste simple
    # arr = np.array([1, 2, 3, 4, 5, 4, 4])
    # x = np.where(arr==4)
    # print(x)#[3,5,6]
    
    matrix = [[1, 2, 3]]
    valeur = 3

    result = my_where(matrix, valeur)
    print(result)  # Output: [(1, 1)]

    
    
    

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")