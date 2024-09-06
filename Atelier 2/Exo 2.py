# 1)
def position1(lstEntier:list, entier:int)-> int:
    """Retourne l'indice de l'entier elt dans la liste lst. Si l'entier elt n'est pas présent dans la liste, la fonction retourne la valeur -1"""
    searchedIndex  = -1
    if len(lstEntier) != 0: 
        for elts in lstEntier :
            if elts == entier:
                searchedIndex = lstEntier.index(entier)
    
    return searchedIndex

def position2(lstEntier:list, entier:int)-> int:
    """Retourne l'indice de l'entier elt dans la liste lst. Si l'entier elt n'est pas présent dans la liste, la fonction retourne la valeur -1"""
    searchedIndex  = -1
    if len(lstEntier) != 0: 
        i = 0
        while searchedIndex == -1 and i < len(lstEntier):
            if entier == lstEntier[i]:
                searchedIndex = lstEntier.index(entier)
            i += 1
    
    return searchedIndex

# print(position2([1,20,33],5))


# 2)
def nb_occurrences(lstEntier:list, entier:int)-> int:
    """retourne le nombre d'occurrences de l'entier dans la liste ."""
    nbOccurence = 0
    if len(lstEntier) != 0: 
        for elts in lstEntier:
            if elts == entier:
                nbOccurence += 1 
    
    return nbOccurence

# print(nb_occurrences([1,20,33,1,2,1],333))

#3)
def est_triee1(lstEntier:list)-> bool:
    """retourne un booléen vrai si la liste est triée par ordre croissant, faux sinon"""
    isSorted = True
    if len(lstEntier) > 1: 
        i= 0
        for i in range(0,len(lstEntier)-1):
            if lstEntier[i] >  lstEntier[i+1] :
                isSorted = False

    return isSorted

def est_triee2(lstEntier:list)-> bool:
    """retourne un booléen vrai si la liste est triée par ordre croissant, faux sinon"""
    isSorted = True
    if len(lstEntier) > 1: 
        i=0
        while i < len(lstEntier)-1 and isSorted:
            if lstEntier[i] > lstEntier[i + 1]:
                isSorted = False
            i +=1
    
    return isSorted

# print(est_triee2([1,2,5,4]))


# 4)

def position_tri(lstEntier:list, entier:int)-> int:
    start= 0
    end = len(lstEntier) - 1 
    middle = 0
    
    while start <= end :
        middle = (start + end) // 2
        if lstEntier[middle] == entier:
            return middle
        elif lstEntier[middle] < entier:
            start = middle + 1
        else :
            end = middle -1
    
    return -1

# print(position_tri(sorted([1,2,5,3]),5))

# 5)

def a_repetitions(lstEntier:list)-> bool:
    lstTampon = []
    isRepeated = False
    if len(lstEntier) > 1:
    #     for elts in lstEntier :
    #         if elts not in lstTampon :
    #              lstTampon.append(elts)
    #         else:
    #             isRepeated = True
        i = 0
        while not isRepeated and i < len(lstEntier):
            if lstEntier[i] not in lstTampon :
                lstTampon.append(lstEntier[i])
            else:
                isRepeated = True
            i +=1
        
    return isRepeated
    
# print(a_repetitions([1,2,3,5,4]))


        
