# ESSENTIELS 
# Exercice 1

# 1)

def somme_v1(L:list)-> int :
    """Retourne la somme des entiers contenu dans la liste L """ 
    somme = 0
    for i in range(0,len(L)):
        somme += L[i]
        
    return somme


def somme_v2(L:list)-> int :
    """Retourne la somme des entiers contenu dans la liste L """ 
    somme = 0
    for e in L:
        somme += e
        
    return somme

def somme_v3(L:list)-> int :
    """Retourne la somme des entiers contenu dans la liste L """ 
    somme=0
    i = 0
    while i < len(L):
        somme += L[i]
        i += 1
        
    return somme
        
# print(sommeV2(laListe))

# La V2 me semble la plus adapté



# 2)

def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_v2([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 11111 : ", somme_v2(lst2test1))

# test_exercice1()


# 3)
def moyenne(L:list)->float:
    """calcul la moyenne de la liste"""
    laMoyenne = 0
    if len(L) != 0 :
        laMoyenne = somme_v2(L)/ len(L)
    
    return laMoyenne

        
def test_moyenne ():
    print("TEST MOYENNE")
    print("Test liste vide : ", moyenne([]))
    lst2test1=[1,10,100, 1000,10000]
    print("Test moyenne: ", moyenne(lst2test1))

# test_moyenne()


# 4)
def nb_sup_v1(L:list, e:int)-> int :
    """retourne le nombre de valeur dans la liste L  strictement supérieur à e """
    nombreValSup = 0
    for i in range(0,len(L)):
        if L[i]  > e :
            nombreValSup += 1
    
    return nombreValSup

def nb_sup_v2(L:list, e:int)-> int :
    """retourne le nombre de valeur dans la liste L  strictement supérieur à e """
    nombreValSup = 0
    for  elmts in L :
        if  elmts > e :
            nombreValSup += 1
    
    return nombreValSup
        
def test_nb_sup():
    print("TEST NOMBRE SUPERIEUR")
    print("Test liste vide : ", nb_sup_v2([],10000000))
    lst2test1=[1,10,100, 1000,10000]
    leNombre = 800
    print("Nombre de valeur supérieur à ",leNombre,": ", nb_sup_v2(lst2test1,leNombre))
    
# test_nb_sup()


# 5)

def moy_sup (L:list,e:int)->float:
    """retourne la moyenne des valeurs de la liste strictement supérieures à e"""
    nombreValSup = nb_sup_v2(L,e)
    sommeSup = 0
    moyenneSup =0
    for elmts in L:
        if elmts > e : 
            sommeSup += elmts
    if nombreValSup != 0 :
        moyenneSup = sommeSup/nombreValSup
                
    return moyenneSup

def test_moy_sup():
    print("TEST NOMBRE SUPERIEUR")
    print("Test liste vide : ", moy_sup([],10000000))
    lst2test1=[1,10,100, 1000,10000]
    leNombre = 800
    print("moyenne des valeur supérieur à ",leNombre,": ", moy_sup(lst2test1,leNombre))

# test_moy_sup()

# 6)
def val_max(L:list)->int:
    """retourne la valeur maximale de la liste l"""
    if len(L)!=0:
        maxVal = L[0]
        for i in range(1,len(L)):
            if maxVal < L[i]:
                maxVal = L[i]
    else :
        maxVal = 0
        
    return maxVal

def test_max():
    print("TEST NOMBRE SUPERIEUR")
    lst2test1=[]
    print("le maximum de  ",lst2test1,"est : ", val_max(lst2test1))
    
# test_max()

#7)
def ind_max(lstEntier:list)->int:
    indexSearched = 0
    if len(lstEntier) != 0:     
        indexSearched = lstEntier.index(val_max(lstEntier)) 
    else:
        # Retourner -1 si la liste est vide
        indexSearched = -1    
    return indexSearched

def test_ind_max():
    print("TEST NOMBRE SUPERIEUR")
    lst2test1=[1,10,100,999,1,999]
    print("le maximum de  ",lst2test1,"est : ", ind_max(lst2test1))
    
# test_ind_max()
