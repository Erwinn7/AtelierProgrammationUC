# def separate(lst:list)->list:
#     separatedList = []
#     for elt in sorted(lst):
#         separatedList.append(elt)
#     return separatedList
# print(separate([1,5,3,0,-4,-9,0,-1,10]))

# def separate(lst:list)->list:
#     """Renvoie la liste entrée avec ses entiers positifs et négatifs séparés"""
#     separatedList= []
#     for elt in lst:
#         if elt < 0:
#             separatedList.insert(0,elt)
#         else:
#             separatedList.append(elt)
#     return separatedList

# print(separate([1,5,3,0,-4,-9,0,-1,10]))
# print('Liste vide : ', separate([]))







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


    # longueur de la liste
    lenLstEntier = len(lstEntier)
    positiveIndex = lenLstEntier -1
    negativeIndex = 0
    # on initialise la liste avec des 0 comme c'est une liste d'entier et la liste a la même taille que lstEntier
    lstLSEP = [0]*lenLstEntier

    for elt in lstEntier:
        # si le nombre est négatif : on le rajoute au début de la liste
        if elt < 0 :
            lstLSEP[negativeIndex] = elt
            negativeIndex += 1
        # si le nombre est positif : on le rajoute à la fin de la liste
        elif elt > 0 :
            lstLSEP[positiveIndex] = elt
            positiveIndex -= 1
        

    return lstLSEP


###TEST a reprendre avec une fonction 

print(separer([3, -2,0, -1, 5, -3, 4,0,0]))
print(separer([]))
print(separer([1,5,2,0]))