
import math

listTypeLettre = ["VERTE","PRIORITAIRE","ECOPLI"]
dicPrioritaire = {"Sticker suivi": 0.50, "OM1":0.05, "OM2":0.11, "20":1.43, "100":2.86, "250":5.26, "500":7.89,"3000":11.44}
dicVerte = {"Sticker suivi": 0.50, "OM1":0.05, "OM2":0.11, "20":1.16 , "100":2.32, "250": 4.00, "500": 6.00, "1000":7.50, "3000":10.50 }
dicEcopli = {"Sticker suivi": 0.50, "OM1":0.02, "OM2":0.05, "20":1.14, "100":2.28, "250":3.92}


def nombre_10g(poidsLettre):    
    return math.ceil(poidsLettre/10)


def montant_affranchissement(poidsLettre, typeLettre,zoneLettre):
    montant = 0.0
    montantBase = 0.0 
    dicUtiliser = {}
    listDesPoids =[]
    
    # verifions le type de lettre existe et choisissons le dictionnaire à utiliser
    if typeLettre in listTypeLettre:
        if typeLettre == "VERTE":
            dicUtiliser = dicVerte
        elif typeLettre == "PRIORITAIRE":
            dicUtiliser = dicPrioritaire
        else : 
            dicUtiliser = dicEcopli
            
        # determinons le poids a choisir  
        
        listDesPoids = list(dicUtiliser.keys())
        listDesPoids.remove("Sticker suivi")
        listDesPoids.remove("OM1")
        listDesPoids.remove("OM2")
   
        poidsTrouve = 0
        
        for elements in listDesPoids:
            if int(elements) < int(poidsLettre) :
                poidsTrouve = 0
            else:
                poidsTrouve = int(elements)
                break
            
        # remplissage des données de calculs
        montantBase = dicUtiliser.get(poidsTrouve)
        montantZone = dicUtiliser.get(zoneLettre)
        nombre10gObtenu = nombre_10g(poidsLettre)
        
        # calcul de complement
        montant = float(montantBase) + float(nombre10gObtenu*montantZone)

    else :
        print("Type de lettre inconnu, Entrez des valeurs existante svp.")
    
    return montant

print( montant_affranchissement(112,"ECOPLI","OM1"),"EUROS")
