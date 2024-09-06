def separer(lstEntier:list)-> list:
    """    Sépare les entiers positifs et négatifs dans une liste.

    Cette fonction prend en entrée une liste d'entiers et renvoie une nouvelle liste
    où tous les entiers négatifs apparaissent en premier, suivis de tous les entiers
    positifs. Les entiers nuls ne sont pas considérés dans cette version du code.

    Paramètres :
    -----------
    lstEntier : list
        Une liste d'entiers à séparer en fonction de leur signe (positif ou négatif).

    Retourne :
    --------
    list
        Une nouvelle liste où les entiers négatifs sont placés au début et les entiers
        positifs à la fin. L'ordre des éléments négatifs et positifs dans la nouvelle 
        liste n'est pas garanti d'être le même que dans la liste d'origine. """

    
    lenLstEntier = len(lstEntier)
    positiveIndex = lenLstEntier -1
    negativeIndex = 0 
    # on initialise la liste avec des 0 comme c'est une liste d'entier 
    LstLSEP = [0]*lenLstEntier 

    
    for elt in lstEntier:
        if elt < 0 :
            LstLSEP[negativeIndex] = elt
            negativeIndex += 1
        elif elt > 0 :
            LstLSEP[positiveIndex] = elt
            positiveIndex -= 1
    
    return LstLSEP

print(separer([3, -2, -1, 5, -3, 4]))
            