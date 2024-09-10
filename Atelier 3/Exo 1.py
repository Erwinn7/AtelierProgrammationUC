"""
Nom du fichier : Exo 1.py
Description : Exercice 1 de l'atelier 3 LST-info-L3
Auteur : Meldi AHISSOU
Date : 10 septembre 2024
"""

import sys

def full_name(nomPrenom: str) -> str:
    """Prend en paramètre une chaine de caractère de type 'nom prenom' et qui renvoie la même chaîne
    avec le nom en majuscule et le prénom avec la première lettre seulement en majuscule.

    Args:
        nomPrenom (str): chaîne de caractères de type 'nom prenom'

    Returns:
        str: la chaîne de caractères formatée
    """
    # On split la chaîne de caractère en une liste de 2 éléments
    resultat = ""
    lstNomPrenom = nomPrenom.split()
    # Si la liste n'est pas vide et le nombre d'élément ne dépasse pas 2
    if len(lstNomPrenom) != 0 and len(lstNomPrenom) == 2 :
        # On met le premier élément en majuscule et le deuxième en capitalisant
        resultat = lstNomPrenom[0].upper() + " " + lstNomPrenom[1].capitalize()
    else:
        resultat = "Entrer une chaine de caractère valide "
    
    return resultat
    
    
def test_full_name()-> None:
    print(full_name("totO BOURGet"))
    print(full_name(""))
    print(full_name("totO BourGET ANDré"))


def verif_corps_or_domaine_ok(chaine:str)-> bool:
    """verifie si la chaine respecte ces conditions : 
    - ne doit pas contenir ‘.’ en premier ou dernier caractère
    - ne doit pas contenir deux ‘.’ concécutifs
    - peut contenir ‘-’ 
    - peut contenir des lettres et des chiffres

    Args:
        chaine (str): la chaine de caractère sur laquelle on veut faire les vérifications

    Returns:
        bool: True si les conditions sont respectés et False sinon
    """
    resultat = False
    if len(chaine) > 0:
            i=-1
            while i < len(chaine)-1 and (chaine[i] != chaine[i+1] or (chaine[i] == chaine[i+1] and chaine[i] != ".")) :
                i += 1
            if i == len(chaine)-1:
                resultat = True
    return resultat

def is_mail(leMail:str)->tuple:
    """vérifie si le mail est valide et renvoie un code d'erreur

    Args:
        leMail (str): le mail à tester

    Returns:
        tuple: le tuple représentant le code d'erreur
    """
    resultat = (1,0)
    if leMail.find("@") != -1 :
        # NB : erreur non gérer pour deux occurence de @ pour respecter les codes erreurs spécifiés
            corps, domaine = leMail.split("@")
            if not verif_corps_or_domaine_ok(corps):
                resultat = (0,1)
            elif not verif_corps_or_domaine_ok(domaine) :
                resultat = (0,3)
            elif domaine.find(".") == -1 :
                resultat = (0,4)

    else :
        # le mail n’est pas valide, il manque l’@
        resultat = (0,2) 
    
    return resultat

    
def test_is_mail(leMail:str)->str:
    """test la fonction is_mail

    Args:
        leMail (str): le mail a tester

    Returns:
        str: le message d'erreur
    """
    dicErrorMessage = { # code erreur : message
                   (1,0):"le mail est valide.",
                   (0,1):"le mail n’est pas valide, le corp n’est pas valide",
                   (0,2):"le mail n’est pas valide, il manque l’@",
                   (0,3):"le mail n’est pas valide, le domaine n’est pas valide",
                   (0,4):"le mail n’est pas valide, il manque le '.' "
                    }
    
    codeErreur = is_mail(leMail)
    message = "Code {} : {} ({})".format(codeErreur, dicErrorMessage.get(codeErreur),leMail)
    
    return message
    
def main():
    """ Point d'entrée du programme."""
    # test_full_name()
    # print(test_is_mail("bi.sgamb.iglia_paul@univ-corse.fr"))
    # print(test_is_mail("..bisgambiglia_paul@univ-corse.fr"))
    # print(test_is_mail(".bisgambiglia_paul.@univ-corse.fr"))
    print(test_is_mail("rbisgambiglia_paulr@runiv-corse.fr"))
    # print(test_is_mail("bisgambiglia_paul@u..niv-corse.fr"))
    # print(test_is_mail("bisgambiglia_paul@univ-corsefr"))
    # print(test_is_mail(".bisgambiglia_paul.@univ-corsefr"))

    
    
    
    
if __name__ == "__main__":
    print("Le script est exécuté directement. \n")
    main()
else:
    print("Le script est importé comme un module.")
    
   


    
    