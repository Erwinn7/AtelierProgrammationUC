import random 
import math
from datetime import date

# Exercice 1

IMC = {'0': 'Rien',
    '16.5': 'Dénutrition ou famine',
       '18.5': 'maigreur',
       '25': 'corpulence normale',
       '30': 'surpoids',
       '35': 'obésité modéré',
       '40': 'obésité sévère',
       math.inf: 'obésité morbide'}


def message_imc(imcUtilisateur:float)->str:
    """Prend en paramètre un imc et renvoie son interprétation"""
    listeDesImc=list(IMC.keys())
    count = 0
    message = ''
    while imcUtilisateur > float(listeDesImc[count]):
        count +=1
    message = IMC.get(listeDesImc[count])

    return message

def test_imc():
    """Génère aléatoirement 10 IMC pour tester la fonction message_imc"""
    for i in range(0,10):
        imcRandom = random.randrange(0,100)
        print('Pour une IMC de : ', imcRandom , ' Vous êtes en : ', message_imc(imcRandom))

#test_imc()



# Exercice 2

def est_bissextile(annee:int)-> bool:
    """Vérifie si l'année entrée est bissextile"""
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False

def test_bissextile():
    """Test la fonction est_bissextile()"""
    print(est_bissextile(2000))
    print(est_bissextile(2100))
    print(est_bissextile(2024))
# test_bissextile()

# Exercice 3

def discriminant(a:float,b:float,c:float)->float:
    """Calcule le discriminant d'une équation du second degré ax²+bx+c=0"""
    delta=b*b - 4*a*c
    return delta

def racine_unique(a:float,b:float)->float:
    """Calcule la racine unique d'une équation du second degré"""
    x = -b / (2*a)
    return x

def racine_double(a:float,b:float,delta:float,num:int)-> float:
    """Calcule la racine double d'une équation du second degré"""
    if num == 1:
        resultat = (- b + math.sqrt(delta)) / (2*a)
    elif num == 2:
        resultat = (- b - math.sqrt(delta)) / (2*a)
    else:
        print('Veuillez entrer un numéro de racine entre 1 et 2')
    return resultat

def str_equation(a:float,b:float,c:float)-> str:
    """Renvoie l'équation du second degré en chaîne de caractères"""
    return '{}x² + {}x + {} =   0'.format(a,b,c)


def solution_equation(a:float,b:float,c:float)-> str:
    """Résoud une équation du second degré"""
    message = ''
    delta=discriminant(a,b,c)
    if delta < 0:
        message = 'Solution de l\'équation {} \n Pas de racine réelle'.format(str_equation(a,b,c))
    elif delta == 0:
        message = 'Solution de l\'équation {} \n Racine unique : x = {}'.format(str_equation(a,b,c),racine_unique(a,b))
    else: 
        message = 'Solution de l\'équation {} \n Deux racines : \n x1 = {} \n x2 = {}'.format(str_equation(a,b,c),racine_double(a,b,delta,1)
        ,racine_double(a,b,delta,2))
    return message

#print(solution_equation(2,1,0))

def equation(a:int,b:int,c:int):
    print(solution_equation(a,b,c))

#equation(2,1,0)

def test_equation():
    equation(1,1,1)
    equation(2,1,0)
    equation(2,-3,9/8)

# test_equation()

# Exercise 4

# Mois : Jours maximum
DICTMOIS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def date_est_valide(jour:int,mois:int,annee:int)-> bool:
    """Vérifie si la date est valide (non valide si supérieur à la date d'aujourd'hui ou si date inexistante)"""
    dateValide = False
    try:
        dateUtilisateur = date(annee,mois,jour)
        if dateUtilisateur <= date.today():
            if est_bissextile(dateUtilisateur.year):
                if dateUtilisateur.month == 2 and 1 <= dateUtilisateur.day <= DICTMOIS.get(dateUtilisateur.month) +1 :
                    dateValide = True
                elif  1 <= dateUtilisateur.day <= DICTMOIS.get(dateUtilisateur.month) and dateUtilisateur.month != 2:
                    dateValide = True
                else:
                    dateValide = False
            else:
                
                if  1 <= dateUtilisateur.month <=12:
                    if 1 <= dateUtilisateur.day <= DICTMOIS.get(dateUtilisateur.month):
                        dateValide = True
    except ValueError:
        dateValide = False    
   

    return dateValide

# print(date_est_valide(28,2,2023))

def saisie_date_naissance()-> date:
    """Demande à l'utilisateur de rentrer sa date et vérifie sa validité"""
    dateResultat = ''
    jour = int(input('Veuillez entrer un jour de naissance'))
    mois = int(input('Veuillez entrer un mois de naissance'))
    annee = int(input('Veuillez entrer une année de naissance'))
    if date_est_valide(jour,mois,annee):

        dateResultat = date(annee, mois, jour)
    else:
        dateResultat = 'Date de naissance invalide'

    return dateResultat
    
#print(saisie_date_naissance())

def age(date_naissance:str)->int:
    """Renvoie l'age de l'utilisateur en fonction de sa date de naissance et de la date d'aujourd'hui"""
    ageUtilisateur=0
    dateAujourdhui = date.today()
    dateNaissanceList = date_naissance.split('/')
    if date_est_valide(int(dateNaissanceList[0]),int(dateNaissanceList[1]),int(dateNaissanceList[2])):
        dateDeNaissanceValide = date(int(dateNaissanceList[2]),int(dateNaissanceList[1]),int(dateNaissanceList[0]))
        # Son anniversaire n'est pas encore passé
        if dateAujourdhui.month < dateDeNaissanceValide.month:
            ageUtilisateur = dateAujourdhui.year - dateDeNaissanceValide.year - 1
        elif dateAujourdhui.month == dateDeNaissanceValide.month:
            # Son anniversaire est dans le mois mais pas encore passé
            if dateAujourdhui.day < dateDeNaissanceValide.day:
                ageUtilisateur = dateAujourdhui.year - dateDeNaissanceValide.year - 1
                # Son anniversaire est passé
            else:
                ageUtilisateur = dateAujourdhui.year - dateDeNaissanceValide.year
        # Calcul de l'age de l'utilisateur
        else:
            ageUtilisateur = dateAujourdhui.year - dateDeNaissanceValide.year
    else:
        print('Date invalide')
    return ageUtilisateur

#print(' B', age('05/09/2020')) 

def est_majeur(date_naissance:str)->bool:
    """Renvoie vrai si l'utilisateur est majeur à partir de sa date de naissance"""
    if age(date_naissance) >= 18:
        return True
    else:
        return False
    
#print(est_majeur('01/01/2010'))

def test_acces()->str:
    date_naissance = input('Veuillez renseigner votre date de naissace (jj/mm/aaaa) :')
    if est_majeur(date_naissance):
        return "Bonjour, vous avez {} ans, Accès autorisé".format(age(date_naissance))
    else:
        return "Désolé, vous avez {} ans, Accès interdit".format(age(date_naissance))
    
print(test_acces())