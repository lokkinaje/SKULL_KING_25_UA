import numpy as np
import random as rd 
import csv 
# === Création du paquet de cartes ===

# Cartes classiques :
# Couleurs : noire (1–14), verte (101–114), violette (201–214), jaune (301–314)
# EXEMPLE_1 : 304 = carte jaune (3) de valeur 4 (04). D'où 304
# EXEMPLE_2 : 213 = carte violette (2) de valeur 13 (13). D'où 213
cartes_noires = np.arange(1, 15)
cartes_vertes = np.arange(101, 115)
cartes_violettes = np.arange(201, 215)
cartes_jaunes = np.arange(301, 315)

# Cartes spéciales :
cartes_pirates = np.arange(401, 406)      # 5 cartes pirates  (401-405)
cartes_fuites = np.arange(601, 606)       # 5 cartes fuite    (601-605)
cartes_sirenes = np.arange(501, 503)      # 2 cartes sirènes  (501-503)
#cartes_tigresse = np.arange(700, 701)     # 1 carte tigresse  (700)
carte_skull_king = np.arange(999, 1000)   # 1 carte Skull King (999) 

# Fusion de toutes les cartes dans un seul tableau (le paquet de cartes)
fu = np.concatenate((
    cartes_noires,
    cartes_vertes,
    cartes_violettes,
    cartes_jaunes,
    cartes_fuites,
    cartes_pirates,
    cartes_sirenes,
    #cartes_tigresse,
    carte_skull_king
))


# === Gestion des joueurs ===

nb_cartes = 70         # Nombre total de cartes dans le paquet
tab_j = []            # Liste des noms des joueurs

# Initialisation des joueurs avec saisie utilisateur
# Initialise les joueurs, demande leurs noms et crée un fichier CSV avec les scores à 0
def init_joueurs():
    global nb_joueurs
    nb_joueurs = 0 
    
    # Demande un nombre de joueurs entre 2 et 6
    while (nb_joueurs < 2) or (nb_joueurs > 6):
        nb_joueurs = int(input("Le nombre de joueurs : "))

    # Saisie des noms des joueurs (en majuscules, sans doublon)
    for i in range(1, nb_joueurs + 1):
        j = input(f'Entrez le nom du Joueur {i}: ').upper()
        while j in tab_j:
            j = input(f'Nom déjà pris ! Entrez un autre nom pour le Joueur {i}: ').upper()
        tab_j.append(j)

# === gestion du fichier CSV
    with open("score_sking.csv" , mode ='w' , newline ='' , encoding ='utf-8') as fichier :
        writer = csv.writer(fichier)
        writer.writerow(["Nom" , "Score"])  #EN-têtes
        for nom in tab_j : 
            writer.writerow([nom , 0]) #Score initial = 0 

    return tab_j

# === Tirage aléatoire d'une carte du paquet ===
# Tire une carte au hasard dans le paquet et la retire du jeu
def tirage() -> int:
    global nb_cartes 
    global fu
    if len(fu) == 0:
        raise ValueError("Plus de cartes dans la pioche.")
    carte = rd.choice(fu)  # tirer une carte au hasard dans la pioche
    ind = np.where(fu == carte)[0][0]
    fu = np.delete(fu, ind)  
    #nb_cartes-=1
    #print(nb_cartes)
    return carte  # Retourne la carte à cet indice

# Distribution des cartes en fonction de la manche
# Gère le déroulement des manches : distribution, mise, jeu, scores
def debut_jeu():
    global nb_cartes 
    global fu 
    global depot 
    nb_manche = 3
    humain = tab_j[0]

    nb_manche = int (input("Entrez le nombre de manche (3-15) : "))
    while (nb_manche < 3 or nb_manche > 10):
        nb_manche = int (input("Erreur! Entrez le nombre de manche : "))


    for manche in range(1,nb_manche +1): #nombre de manches
        print(f'=== Manche {manche} ====')
        mains = []
        if manche > 1:
            rotation_premier_joueur(tab_j)
            rotation_premier_joueur(tab_scores)
        #Distribuer 'manche' cartes à chaque joueur
        #Demander la mise de chaque utilisateur 
        for _ in range(len(tab_j)) : 
            mains.append([tirage() for _ in range(manche)])
            #print (fu)
        
        for i in range(nb_joueurs):
            if tab_j [i] == humain:
                
                print(f'Main de {tab_j[i]} : {mains[i]}')
            else:
                print(f'Main de {tab_j[i]} : (Invisible pour les autres joueurs) ')
            
            dico_tg = {}
            for name in tab_j:
                dico_tg[name] = 0   #initialisation des tours gagnés à 0

            dico_j = {}
            for name in tab_j:
                dico_j[name] = 0   #initialisation des tours gagnés à 0

        for i in range (len(tab_j)) : 
            if tab_j[i] == humain :
                mise(dico_j , tab_j[i] , manche ,i)
            else : 
                mise_automatique (dico_j , tab_j[i] ,  manche , mains[i] , i )

        # Chaque joueur joue une carte à chaque "tour"
        for tour in range(manche):
            depot = []  # Autant de tours que de cartes
            for i in range(nb_joueurs):
                if tab_j[i] == humain :
                    choisir_carte(mains[i], i)
                else:
                    choisir_cartes_automatique(dico_j ,dico_tg , mains[i] , depot , mains[i]  , i  )

            print(f" La carte la plus forte : {comparaison(depot)}")
            indices = [i for i , x in enumerate(depot) if x == comparaison(depot)]
            print(indices)
            print (tab_j[indices[0]]) #affiche le nom du joueur qui a gagné le tour
            nombre_de_tours_gagné(dico_tg,tab_j[indices[0]])
            fu = np.concatenate ((fu , depot))
            
        tableau_des_scores(dico_j,dico_tg,manche)
        enregistrer_scores_csv(tab_j,tab_scores)
        
        print(f' Main finale: {mains}')
            
        
def abs(x):
    if (x >= 0):
        return x
    return -x
def mise (dico_j , nom : str , limit_de_mise :int , i):
    m = int(input(f"{tab_j[i]} Entrez votre mise : "))
    while(m > limit_de_mise or m < 0):
        m = int(input(f"Valeur incorrecte ! {tab_j[i]} Entrez votre mise : "))

    dico_j[nom] = m
    print(dico_j)
    return dico_j
# Permet au joueur humain de choisir une carte à jouer dans sa main
def choisir_carte(mains : list , i ) ->int :
    
    if len(mains) == 1 :
        d = mains[0]
        '''
        if d == 700 :   

            fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p'): ")
            while (fuite_ou_pirate != 'f' and 
                fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'P'    and 
                fuite_ou_pirate != 'F' and
                fuite_ou_pirate != 'fuite' and 
                fuite_ou_pirate != 'pirate' and 
                fuite_ou_pirate != 'FUITE' and 
                fuite_ou_pirate != 'PIRATE') :
                fuite_ou_pirate = input("Erreur de syntaxe ! Tigresse permet de choisir entre fuite ('f') ou pirate ('p'): ")
            if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate =='F' or fuite_ou_pirate == 'FUITE': 
                d = 601
                mains.remove(mains[0])
                #print (f'carte(s) restante(s) dans la main : {mains}')
                recup_cartes(d) 
                return d

            else : 
                d = 401 
                mains.remove(mains[0])
                #print (f'carte(s) restante(s) dans la main : {mains}')
                recup_cartes(d)
                return d
            '''
        mains.remove(mains[0])
        #print(f'carte(s) restante(s) dans la main : {mains}') 
        recup_cartes(d) 
        return d
    
    else : 
        c = int(input(f"{tab_j[i]} choisissez une carte : "))
        while c not in mains  : 
            c = int(input(f" carte non présente, {tab_j[i]} choisissez une carte : "))
        d = c
        '''
        if d == 700 :   

            fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p'): ")
            while (fuite_ou_pirate != 'f' and 
                fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'P'    and 
                fuite_ou_pirate != 'F' and
                fuite_ou_pirate != 'fuite' and 
                fuite_ou_pirate != 'pirate' and 
                fuite_ou_pirate != 'FUITE' and 
                fuite_ou_pirate != 'PIRATE') :
                fuite_ou_pirate = input("Erreur de syntaxe ! Tigresse permet de choisir entre fuite ('f') ou pirate ('p'): ")
            if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate =='F' or fuite_ou_pirate == 'FUITE': 
                d = 601
                mains.remove(c)
                #print (f'carte(s) restante(s) dans la main : {mains}')
                recup_cartes(d) 
                return d

            else : 
                d = 401 
                mains.remove(c)
                #print (f'carte(s) restante(s) dans la main : {mains}')
                recup_cartes(d)
                return d 
        '''
        mains.remove(c)
        #print (f'carte(s) restante(s) dans la main : {mains}')
        recup_cartes(d) 
        return d  
    
def maximum_des_deux (a , b ) : 
    if a > b : 
        return a 
    return b 

# === fonction de comparaison entre tous les cartes jouables 
# Compare les cartes jouées et retourne la plus forte selon les règles
def comparaison(depot) :
    carte_max = depot[0]
    for i in range(1,len(depot)):

        if carte_max in cartes_noires :
            carte_max = comparaison_noir_vers_tous(carte_max, depot[i])
        
        elif carte_max in cartes_vertes :
            carte_max = comparaison_vert_vers_tous(carte_max,depot[i])

        elif carte_max in cartes_jaunes :
            carte_max = comparaison_jaune_vers_tous(carte_max,depot[i])

        elif carte_max in cartes_violettes :
            carte_max = comparaison_violet_vers_tous(carte_max,depot[i])

        elif carte_max in cartes_fuites :
            carte_max = comparaison_fuite_vers_tous(carte_max,depot[i])

        elif carte_max in cartes_pirates :
            carte_max = comparaison_pirates_vers_tous(carte_max,depot[i])

        elif carte_max in cartes_sirenes :
            carte_max = comparaison_sirene_vers_tous(carte_max,depot[i])

        elif carte_max in carte_skull_king :
            carte_max = comparaison_sking_vers_tous(carte_max,depot[i])
        
        # elif carte_max in cartes_tigresse :
        #     carte_max =  comparaison_tigresse_vers_tous(carte_max,depot[i])
    return carte_max
    

# === fonction de comparaison entre les cartes noirs et les autres cartes du jeu === 
        
# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_noir_vers_tous(noir , autre ) :

    #  Cas lorsque la carte jouée est une carte vertes violettes, jaunes ou une carte de fuite 
    if (autre >= 101 and autre < 315 ) or (autre >= 601 and autre < 606 ) : 
        return noir  # victoire pour la carte prioritaire noire 
    
    # Si l'autre carte jouée est une carte noire
    elif  (autre >=  1 and autre < 15 ) :  
        return maximum_des_deux(noir , autre ) # victoire pour la carte de plus grande valeur 
    '''
    # Cas particulier de la carte tigresse qui peut être jouer en carte fuite ou en pirates 
    elif (autre == 700) : 

        #demande à l'utilisateur son choix entre fuite et pirate 
        fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p'), entrez votre choix : ")
        while (fuite_ou_pirate != 'f' and fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'F' and fuite_ou_pirate != 'P'    and 
            fuite_ou_pirate != 'fuite' and fuite_ou_pirate != 'pirate') :
            fuite_ou_pirate = input("Erreur de syntaxe ! Entrez votre choix: ")
        if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate != 'F' : 
            return noir  # fuite perd contre tous les cartes donc noir gagne 
        return autre # dans l'autre cas c'est pirate qui gagne car pirate à la priorité sur les cartes noires
    '''
    # Cas des cartes pirates ,sirènes et skull king 
    return autre
    
# === comparaison des cartes vertes avec les autre cartes du jeu 
# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_vert_vers_tous (vert , autre ) : 

    # cas ou l'autre cartes est une carte vertes
    if (autre >= 101 and autre <= 114) :
        return maximum_des_deux (vert , autre ) # retour de la carte avec la valeur la plus grande 
    
    # Cas des cartes violettes, jaunes et fuites  
    elif (autre >= 201 and autre <= 314) or (autre >= 601 and autre < 606 ) : 
        return vert 
    '''
    # Cas particulier de la carte tigresse qui peut être jouer en carte fuite ou en pirates 
    elif (autre == 700) : 

        #demande à l'utilisateur son choix entre fuite et pirate 
        fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")
        while (fuite_ou_pirate != 'f' and fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'F' and fuite_ou_pirate != 'P'    and 
            fuite_ou_pirate != 'fuite' and fuite_ou_pirate != 'pirate') :
            fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")

        if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate != 'F' : 
            return vert  # fuite perd contre tous les cartes donc noir gagne 
        return autre # dans l'autre cas c'est pirate qui gagne car pirate à la priorité sur les cartes vertes
    ''' 
    
    # Cas des cartes pirates ,sirènes et skull king 
    return autre

# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_violet_vers_tous (violet  , autre ) : 

    # cas ou l'autre cartes est une carte violettes 
    if (autre >= 201 and autre <= 214) :
        return maximum_des_deux (violet , autre ) # retour de la carte avec la valeur la plus grande 
    
    # Cas des cartes vertes ,jaunes et fuites 
    elif (autre >= 101 and autre <= 114)  or (autre >= 301 and autre <= 314  )  or (autre >= 601 and autre < 606 ) :  
        return violet 
    '''
    # Cas particulier de la carte tigresse qui peut être jouer en carte fuite ou en pirates
     
    elif (autre == 700) : 

        #demande à l'utilisateur son choix entre fuite et pirate 
        fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")
        while (fuite_ou_pirate != 'f' and fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'F' and fuite_ou_pirate != 'P'    and 
            fuite_ou_pirate != 'fuite' and fuite_ou_pirate != 'pirate') :
            fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")

        if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate != 'F' : 
            return violet   # fuite perd contre tous les cartes donc noir gagne 
        return autre # dans l'autre cas c'est pirate qui gagne car pirate à la priorité sur les cartes vertes
    '''
    
    # Cas des cartes pirates ,sirènes et skull king
    return autre

# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_jaune_vers_tous (jaune , autre ) : 

    # cas ou l'autre cartes est une carte jaunes 
    if (autre >= 301 and autre <= 314) :
        return maximum_des_deux (jaune , autre ) # retour de la carte avec la valeur la plus grande 
    
    # Cas des cartes vertes, violletes et de fuites  
    elif (autre >= 101 and autre <= 214) or (autre >= 601 and autre <= 605 ) : 
        return jaune 
    '''
    # Cas particulier de la carte tigresse qui peut être jouer en carte fuite ou en pirates 
    elif (autre == 700) : 

        #demande à l'utilisateur son choix entre fuite et pirate 
        fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")
        while (fuite_ou_pirate != 'f' and fuite_ou_pirate != 'p'    and 
                fuite_ou_pirate != 'F' and fuite_ou_pirate != 'P'    and 
            fuite_ou_pirate != 'fuite' and fuite_ou_pirate != 'pirate') :
            fuite_ou_pirate = input("Tigresse permet de choisir entre fuite ('f') ou pirate ('p')")

        if fuite_ou_pirate == 'f' or fuite_ou_pirate == 'fuite' or fuite_ou_pirate != 'F' : 
            return jaune  # fuite perd contre tous les cartes donc noir gagne 
        return autre # dans l'autre cas c'est pirate qui gagne car pirate à la priorité sur les cartes vertes
    ''' 
    
    # Cas des cartes pirates ,sirènes et skull king 
    return autre


# === comparaison des cartes pirates avec les autres cartes 
# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_pirates_vers_tous (pirate , autre ) :
    
    # comparaison avec la carte Skull King 
    if (autre == 999) : 
        return autre  # perd contre le skull king 
    return pirate # gagne contre toutes les autres cartes du jeu 


# === comparaison des cartes SKULL KING avec toutes les autres 
# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_sking_vers_tous (sking , autre) :

    #comparaison avec les cartes sirènes 
    if (autre <= 502 and autre  >= 501 ) : 
        return autre # perd contre les cartes sirènes 
    return sking #gagne contre toutes les autres cartes 


# === Comparaison des cartes sirènes contre toutes les autres cartes 
# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_sirene_vers_tous (sirene , autre ) :

    # Comparaion contre les cartes pirates 
    if (autre >= 401 and autre < 406 ) :  
        return autre # perd contre les cartes pirates 
    
    return sirene #gagne contre toutes les les autres cartes 



# Fonctions spécifiques de comparaison entre types de cartes
def comparaison_fuite_vers_tous (fuite , autre) : 
    if autre in cartes_fuites  : 
        return fuite 
    return autre 
depot = []
# Ajoute une carte au dépôt (cartes jouées pendant un tour)
def recup_cartes (carte: int) -> list:
    global depot 
    depot.append(carte)
    print(f'Jeu courant : {depot}')
    return depot
# === score selon Rascal ===
#fonction qui calcul le nombre de tours gagné par Chaque joueurs
# Incrémente le nombre de tours gagnés pour un joueur
def nombre_de_tours_gagné (dico_tg:dict, nom:str) -> dict:
    dico_tg[nom] += 1
    print(f'Score de la manche : {dico_tg}')
    return dico_tg

tab_scores = []


# Calcule et affiche les scores de chaque joueur à la fin de la manche
def tableau_des_scores(dico_j,dico_tg,manche) -> list:
    gagne = manche*10
    presque_gagne = manche*5
    global tab_scores

    if manche == 1 : 
        for i in range (len(tab_j)):
            tab_scores.append(0) 

    for i in range (len(tab_j)) :
        if dico_j[tab_j[i]] == dico_tg[tab_j[i]] : 
            tab_scores[i]+=gagne
            print (f'{tab_j[i]} a gagné {gagne} points'  )
        elif abs(dico_j[tab_j[i]] - dico_tg[tab_j[i]]) == 1:
            print (f'{tab_j[i]} a gagné {presque_gagne} points'  )
            tab_scores[i]+=presque_gagne
        else :
            print (f'{tab_j[i]} a gagné {manche * 0 } points'  )
            tab_scores[i]+=0 

    print(tab_scores)

# Écrit les scores dans un fichier CSV à chaque fin de manche
def enregistrer_scores_csv(tab_j, tab_scores):
    with open("score_sking.csv", mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Score"])  # En-têtes
        for nom, score in zip(tab_j, tab_scores):
            writer.writerow([nom,score])



#fonction qui choisi un carte aléatoire
# Permet au joueur humain de choisir une carte à jouer dans sa main
def choisir_cartes_aleatoire(mains , i):
    if len(mains) == 1 :
        d = mains[0]
        mains.remove(mains[0])
        #print(f'carte(s) restante(s) dans votre main : {mains}') 
        recup_cartes(d) 
        return d
    else : 
        c = rd.choice(mains)
        #print(f"Joueur {tab_j[i]} choisissez une carte : {c}")
        while c not in mains  : 
            c = rd.choice(mains)
            #print(f"Erreur ! Joueur {tab_j[i]} choisissez une carte : {c}")
           
        d = c 
        mains.remove(c)
        #print (f'carte(s) restante(s) dans votre main : {mains}')
        recup_cartes(d) 
        return d  
    
# L'IA effectue automatiquement une mise en fonction des cartes qu'elle a
def mise_automatique (dico_j ,nom : str  ,  manche , mains , i ):
    faibles = np.concatenate ((cartes_jaunes,cartes_vertes,cartes_violettes))
    mid = cartes_noires
    fortes = np.concatenate((cartes_pirates,cartes_sirenes,carte_skull_king))
    nb_faibles = 0
    nb_mid = 0
    nb_fortes= 0

    valeur_des_faibles = 0
    valeur_des_mid = 1
    valeur_des_fortes = 1

    for c in mains:
        if c in faibles:
            nb_faibles += 1
        elif c in mid:
            nb_mid += 1
        else:
            nb_fortes += 1

    if manche < 4:
        mise_a = valeur_des_faibles*nb_faibles + valeur_des_mid*nb_mid + valeur_des_fortes*nb_fortes
        dico_j[nom] = mise_a
        #print(dico_j)
        print (f"{tab_j[i]} a misé : {mise_a} ")
        return mise_a 
    else:
        mise_a = 0 
        mise_a = mise_a + (nb_faibles // 3 ) + (nb_mid //2 ) + (nb_fortes * valeur_des_fortes )
        dico_j[nom] = mise_a
        #print(dico_j)
        print (f"{tab_j[i]} a misé : {mise_a} ")
        return mise_a 

    
# Permet au joueur humain de choisir une carte à jouer dans sa main
def choisir_cartes_automatique( dico_j , dico_tg , mains , depot , main  , i : int  ) : 

    if len(depot) == 0 : 
        d = comparaison(main)
        ''' 
        if d == 700 :
            print((f"Tigresse permet de choisir entre fuite ou pirate: "))
            d_bis  = 401
            print((f" {tab_j[i]} joue la carte pirate  "))
            mains.remove(d)
            print (f'carte(s) restante(s) dans la main  {mains}')
            recup_cartes(d_bis) 
            return d_bis 
        else:
        '''
        mains.remove(d)
        #print (f'carte(s) restante(s) dans la main  {mains}')
        recup_cartes(d) 
        return d
    

    else :
        if dico_j[tab_j[i]] > dico_tg [tab_j[i]] : 

            d = comparaison(main) 
            '''
            if d == 700 :
                print((f"Tigresse permet de choisir entre fuite ou pirate: "))
                d_bis  = 401
                print((f" {tab_j[i]} joue la cacomparaison_sking_vers_tousrte pirate  "))
                mains.remove(d)
                print (f'carte(s) restante(s) dans la main  {mains}')
                recup_cartes(d_bis) 
                return d_bis 
            else :
            '''                
            mains.remove(d)
            #print(f'carte(s) restante(s) dans la main : {mains}') 
            recup_cartes(d) 
            return d
            
        else : 
            d = comparaison(main)
            ''''
            if d == 700 :
                print((f"Tigresse permet de choisir entre fuite ou pirate "))
                d_bis  = 601
                print((f" {tab_j[i]} joue la carte fuite  "))
                mains.remove(d)
                print (f'carte(s) restante(s) dans la main : {mains}')
                recup_cartes(d_bis) 
                return d_bis 
        '''
            return choisir_cartes_aleatoire(main , i )


# Fait tourner les joueurs : le premier passe à la fin
def rotation_premier_joueur(tab_j):
  tab_j.append(tab_j.pop(0))
  return tab_j
'''
def strategie_2():
    if len(depot) == 0:
        return choisir_cartes_automatique( dico_j , dico_tg , mains , depot , main  , i : int )
    elif len(depot) > 0:    #s'il y a des cartes dans le dépot
        carte_max_du_depot = comparaison(depot)   #On prend la carte la plus forte du depot
        if carte_max_du_depot in faibles:    #On regarde si c'est une carte faible
            if  mise_automatique (dico_j ,nom : str  ,  manche , mains , i ) <= 1: #on verifie si laa mise faite est 0 ou 1
                return min(mains[i]) #alors on retourne la carte la plus faible (pour "respecter" la mise)
            else: 
                return comparaison(mains[i]) #sinon si la mise est supérieur à 1 on retourne la carte la plus faible
        elif carte_max_du_depot in fortes:
'''
# Identifie le joueur avec le score le plus élevé à la fin de la partie
def vainqueur(tab_j,tab_scores):
    indice_max = 0
    for i in range (1,len(tab_scores)):
        if (tab_scores[i] > tab_scores[indice_max]):
            indice_max = i
    return tab_j[indice_max]

# === Fonction principale ===
# Point de départ du jeu : lance l'initialisation et le déroulement du jeu
def main():
    init_joueurs()   # Etape 1 : demander les joueurs
    debut_jeu()        #Etape 2 : mise en place du jeu
    print(f'{vainqueur(tab_j,tab_scores)} est le vainqueur du jeu')
   
     
# === Point d'entrée du programme ===
if __name__ == '__main__':
    main()
