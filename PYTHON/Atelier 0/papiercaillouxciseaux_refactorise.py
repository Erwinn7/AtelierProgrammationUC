#  <body> 

import random

scoreJoueur1 = 0
nombreDePartie = 0
is_enCours = True
scoreJoueur2 = 0

contreIA = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
        
if contreIA == 'O':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble \n")
    nomJoueur2 = 'Machine'
    
elif contreIA == 'N':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble")
    nomJoueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nomJoueur2, " nous allons jouer ensemble \n")
    
else:
    print("Je n'ai pas compris votre réponse")


while is_enCours:
    nombreDePartie += 1 
    c1 = input(nomJoueur1,"faîtes votre choix parmi (pierre, papier, ciseaux): ")
    if c1 != 'pierre':
        if c1 != 'papier':
            if c1 != 'ciseaux':
                c1ok = False
                print("Je n'ai pas compris votre réponse")
                while c1ok == False :
                    print("Joueur ", nomJoueur1)
                    c1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                    c1ok = True
                    if c1 != 'pierre': 
                        if c1 != 'papier':
                            if c1 != 'ciseaux':
                                c1ok = False

    if nomJoueur2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que contreIA == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        e2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]


    if nomJoueur2 != 'Machine':
        print("Joueur", nomJoueur2)
        e2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if e2 != 'pierre':
            if e2 != 'papier':
                if e2 != 'ciseaux':
                    j2bon = False
                    print("Je n'ai pas compris votre réponse")
                    while not j2bon :
                        print("Joueur ", nomJoueur2)
                        e2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                        j2bon = True
                        if e2 != 'pierre': 
                            if e2 != 'papier':
                                if e2 != 'ciseaux':
                                    j2bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nomJoueur1, c1, "et", nomJoueur2, e2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if c1 == 'papier' and e2 == 'papier' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'papier' :
        w12 = nomJoueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'pierre' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'ciseaux' :
        w12 = nomJoueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'papier' and e2 == 'ciseaux' :
        w12 = nomJoueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'papier' and e2 == 'pierre' :
        w12 = nomJoueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'pierre' :
        w12 = nomJoueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'ciseaux' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'papier' :
        w12 = nomJoueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, s1, "et", nomJoueur2, p2, "\n")

    if nombreDePartie ==1 or nombreDePartie ==2 or nombreDePartie==3 or nombreDePartie==4:
        is_enCours = True
    if nombreDePartie ==5:
        is_enCours = False
        
    if nombreDePartie ==1 or nombreDePartie ==2 or nombreDePartie==3 or nombreDePartie==4:
        #On propose de c ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJoueur1,nomJoueur2))
        if go == 'O':
            is_enCours = True
        if go == 'N':
            is_enCours = False
        if go != 'O' and go != 'N':
            is_enCours = True
            print("Vous ne répondez pas à la question, on continue ")
  
        
print("Merci d'avoir joué ! A bientôt")