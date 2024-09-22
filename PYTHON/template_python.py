"""
Nom du fichier : exemple.py
Description : Ce fichier contient un exemple de bonnes pratiques en Python.
Auteur : Votre Nom
Date : 10 septembre 2024
"""

import sys

def ma_fonction_principale(param1, param2):
    """
    Fonction principale de l'exemple.

    Args:
        param1 (int): Le premier paramètre.
        param2 (str): Le deuxième paramètre.

    Returns:
        bool: Le résultat de l'opération.
    """
    if param1 > 0:
        print(f"Le paramètre 1 est positif : {param1}")
        return True
    else:
        print(f"Le paramètre 1 est négatif ou nul : {param1}")
        return False

def une_autre_fonction():
    """
    Une autre fonction pour illustrer les bonnes pratiques.

    Returns:
        None
    """
    print("Ceci est une autre fonction.")

def fonction_avec_parametres(param1, param2):
    """
    Fonction qui prend plusieurs paramètres.

    Args:
        param1 (int): Le premier paramètre.
        param2 (str): Le deuxième paramètre.

    Returns:
        str: Une chaîne de caractères combinant les deux paramètres.
    """
    return f"Paramètre 1 : {param1}, Paramètre 2 : {param2}"

def main():
    """
    Point d'entrée du programme.
    """
    # Déclaration d'une variable
    ma_variable = 42
    print(f"Valeur de ma_variable : {ma_variable}")

    # Exemple d'utilisation des fonctions
    resultat = ma_fonction_principale(10, "exemple")
    print(f"Résultat de la fonction principale : {resultat}")
    une_autre_fonction()

    # Appel de la fonction avec plusieurs paramètres
    resultat_fonction = fonction_avec_parametres(ma_variable, "texte")
    print(f"Résultat de la fonction avec paramètres : {resultat_fonction}")

    # Utilisation de __file__
    print(f"Le nom du fichier est : {__file__}")

    # Utilisation de sys.argv
    if len(sys.argv) > 1:
        print(f"Arguments passés au script : {sys.argv[1:]}")
    else:
        print("Aucun argument passé au script.")

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")