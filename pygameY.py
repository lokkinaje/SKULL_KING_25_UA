"""

   Projet de concrétisation L1 MI 2A groupe 7 
   de MAI a JUIN 2025 
   programmeurs : KLIKO Merveille & BA Aminata Tako 


"""
#=================================================================================
# IMPORTS 
#=================================================================================

import pygame
import time
import numpy as np 

from bouton import Button 
import  concretisation_C as CD 


#=================================================================================
# INITIALISATION 
#=================================================================================

#initialisation de la fenêtre 
pygame.init() #initialisation du pygame
HD  = (1200,800) # définiton d'une fenètre HD en 16:9 
ecran = pygame.display.set_mode(HD) #défintion de la fenetre d'affichage 

#Icone et titre 
pygame.display.set_caption('SKULL KING ') #écriture du nom de l'app 
icon = pygame.image.load("pirate.png") #chargement de l'icon de l'app  
pygame.display.set_icon(icon) #mis en place de l'icon 



#=================================================================================
# CHARGEMENT DES CARTES 
#=================================================================================

# === VUE DE DOS DES CARTES === 
dos_carte = pygame.image.load('cartes_sk/arriere_carte.png') #image d'arrière plan

# === CARTES NOIRES ===
carte_noire_1  = pygame.image.load('cartes_sk/carte_noire_1.png') #image d'arrière plan
carte_noire_2= pygame.image.load('cartes_sk/carte_noire_2.png') #image d'arrière plan
carte_noire_3 = pygame.image.load('cartes_sk/carte_noire_3.png') #image d'arrière plan

carte_noire_4 = pygame.image.load('cartes_sk/carte_noire_4.png') #image d'arrière plan
carte_noire_5 = pygame.image.load('cartes_sk/carte_noire_5.png') #image d'arrière plan
carte_noire_6 = pygame.image.load('cartes_sk/carte_noire_6.png') #image d'arrière plan

carte_noire_7 = pygame.image.load('cartes_sk/carte_noire_7.png') #image d'arrière plan
carte_noire_8 = pygame.image.load('cartes_sk/carte_noire_8.png') #image d'arrière plan
carte_noire_9 = pygame.image.load('cartes_sk/carte_noire_9.png') #image d'arrière plan

carte_noire_10 = pygame.image.load('cartes_sk/carte_noire_10.png') #image d'arrière plan
carte_noire_11 = pygame.image.load('cartes_sk/carte_noire_12.png') #image d'arrière plan
carte_noire_12= pygame.image.load('cartes_sk/carte_noire_12.png') #image d'arrière plan

carte_noire_13 = pygame.image.load('cartes_sk/carte_noire_13.png') #image d'arrière plan
carte_noire_14 = pygame.image.load('cartes_sk/carte_noire_14.png') #image d'arrière plan

# === CARTES VERTES ===

carte_verte_1  = pygame.image.load('cartes_sk/carte_verte_1.png') #image d'arrière plan
carte_verte_2  = pygame.image.load('cartes_sk/carte_verte_2.png') #image d'arrière plan
carte_verte_3  = pygame.image.load('cartes_sk/carte_verte_3.png') #image d'arrière plan

carte_verte_4  = pygame.image.load('cartes_sk/carte_verte_4.png') #image d'arrière plan
carte_verte_5 = pygame.image.load('cartes_sk/carte_verte_5.png') #image d'arrière plan
carte_verte_6  = pygame.image.load('cartes_sk/carte_verte_6.png') #image d'arrière plan

carte_verte_7  = pygame.image.load('cartes_sk/carte_verte_7.png') #image d'arrière plan
carte_verte_8  = pygame.image.load('cartes_sk/carte_verte_8.png') #image d'arrière plan
carte_verte_9  = pygame.image.load('cartes_sk/carte_verte_9.png') #image d'arrière plan

carte_verte_10  = pygame.image.load('cartes_sk/carte_verte_10.png') #image d'arrière plan
carte_verte_11  = pygame.image.load('cartes_sk/carte_verte_11.png') #image d'arrière plan
carte_verte_12  = pygame.image.load('cartes_sk/carte_verte_12.png') #image d'arrière plan

carte_verte_13  = pygame.image.load('cartes_sk/carte_verte_13.png') #image d'arrière plan
carte_verte_14  = pygame.image.load('cartes_sk/carte_verte_14.png') #image d'arrière plan


# === CARTES JAUNES ===

carte_jaune_1  = pygame.image.load('cartes_sk/carte_jaune_1.png') #image d'arrière plan
carte_jaune_2  = pygame.image.load('cartes_sk/carte_jaune_2.png') #image d'arrière plan
carte_jaune_3  = pygame.image.load('cartes_sk/carte_jaune_3.png') #image d'arrière plan

carte_jaune_4  = pygame.image.load('cartes_sk/carte_jaune_4.png') #image d'arrière plan
carte_jaune_5 = pygame.image.load('cartes_sk/carte_jaune_5.png') #image d'arrière plan
carte_jaune_6 = pygame.image.load('cartes_sk/carte_jaune_6.png') #image d'arrière plan

carte_jaune_7  = pygame.image.load('cartes_sk/carte_jaune_7.png') #image d'arrière plan
carte_jaune_8  = pygame.image.load('cartes_sk/carte_jaune_8.png') #image d'arrière plan
carte_jaune_9  = pygame.image.load('cartes_sk/carte_jaune_9.png') #image d'arrière plan

carte_jaune_10  = pygame.image.load('cartes_sk/carte_jaune_10.png') #image d'arrière plan
carte_jaune_11  = pygame.image.load('cartes_sk/carte_jaune_11.png') #image d'arrière plan
carte_jaune_12 = pygame.image.load('cartes_sk/carte_jaune_12.png') #image d'arrière plan

carte_jaune_13  = pygame.image.load('cartes_sk/carte_jaune_13.png') #image d'arrière plan
carte_jaune_14  = pygame.image.load('cartes_sk/carte_jaune_14.png') #image d'arrière plan



# === CARTES VIOLETTES ===

carte_violette_1  = pygame.image.load('cartes_sk/carte_violette_1.png') #image d'arrière plan
carte_violette_2  = pygame.image.load('cartes_sk/carte_violette_2.png') #image d'arrière plan
carte_violette_3  = pygame.image.load('cartes_sk/carte_violette_3.png') #image d'arrière plan

carte_violette_4  = pygame.image.load('cartes_sk/carte_violette_4.png') #image d'arrière plan
carte_violette_5  = pygame.image.load('cartes_sk/carte_violette_5.png') #image d'arrière plan
carte_violette_6  = pygame.image.load('cartes_sk/carte_violette_6.png') #image d'arrière plan

carte_violette_7  = pygame.image.load('cartes_sk/carte_violette_7.png') #image d'arrière plan
carte_violette_8  = pygame.image.load('cartes_sk/carte_violette_8.png') #image d'arrière plan
carte_violette_9  = pygame.image.load('cartes_sk/carte_violette_9.png') #image d'arrière plan

carte_violette_10  = pygame.image.load('cartes_sk/carte_violette_10.png') #image d'arrière plan
carte_violette_11 = pygame.image.load('cartes_sk/carte_violette_11.png') #image d'arrière plan
carte_violette_12 = pygame.image.load('cartes_sk/carte_violette_12.png') #image d'arrière plan

carte_violette_13 = pygame.image.load('cartes_sk/carte_violette_13.png') #image d'arrière plan
carte_violette_14 = pygame.image.load('cartes_sk/carte_violette_14.png') #image d'arrière plan


# === CARTES SIRENES === 

carte_sirene_1 = pygame.image.load('cartes_sk/carte_sirene_1.png') #image d'arrière plan
carte_sirene_2 = pygame.image.load('cartes_sk/carte_sirene_2.png') #image d'arrière plan

# === CARTES PIRATE === 

carte_pirate = pygame.image.load('cartes_sk/face_pirate.png') #image d'arrière plan


# === CARTE TIGRESSE  === 

carte_tigresse = pygame.image.load('cartes_sk/face_tigresse.png') #image d'arrière plan

# === CARTES FUITE ===
carte_fuite = pygame.image.load('cartes_sk/carte_fuite.png') #image d'arrière plan

# === CARTES FUITE ===
carte_sk = pygame.image.load('cartes_sk/carte_sk.jpg') #image d'arrière plan



                              
#=================================================================================
# VARIABLES GLOBALES
#=================================================================================
texte_info = "Bienvenue dans Skull King ! Règles du jeu : 1. Chaque joueur reçoit des cartes. 2. Il faut miser le bon nombre de plis.3. Les pirates battent les sirènes, sauf exceptions...4. Le Skull King bat tout... sauf les sirènes !5. Un pli = une manche.6. Points bonus si tu mises bien !7. Partie en 10 manches.8. Bonne chance moussaillon !"

manche_actuelle = 1 

one_tour = True 

scroll_y = 0

# === Les couleurs  === 
couleur_blanche = (255 , 255 , 255 ) # blanc 
couleur_noire = (0 , 0 , 0 ) #  noir 
couleur_rouge = (255 , 0 , 0) # rouge 
couleur_verte = ( 0 , 255 , 0 ) # vert 
couleur_bleue = ( 0 , 0 , 255 ) # bleu 
couleur_grise = ( 200 , 200 , 200 ) #gris sombre 
couleur_grise_clair = (50 , 50 , 50 ) #gris clair  
couleur_or = (212, 175, 55)  #  or
couleur_bordure = (255, 215, 0)  # jaune doré plus vif

# Zone de saisie (rectangle)
zone_saisie_rect = pygame.Rect(150, 300, 200, 80)  # position x, y, largeur, hauteur

#initialisation du fixeur 
fixeur = True #initialisé à True (pour dire que le programme fonctionne )

#initialisation du mixer sonor (musique médiéval/pirate )
pygame.mixer.init()

#police de l'écriture "SKULL KING" et 'pirate.ttf' (fichier inclus dans le dossier)
font_sking = pygame.font.Font("pirate.ttf", 160) 
font_ecriture = pygame.font.Font( "pirate.ttf" , 80)

# font_basique = pygame.font.SysFont( , 100 )

#texte principale du SKULL KING 
texte_principale = font_sking.render("SKULL KING", True, couleur_blanche) #blanc  
surbrillance = font_sking.render("SKULL KING", True, couleur_noire ) #rouge 

#texte du bouton de départ
position_bouton_depart  = (400,500) #position du bouton de lancement
bouton_depart = Button("image_bouton.png" , position_bouton_depart , 1)


position_continuer_nombres_joueurs  = (400 + 110  ,500) #position du bouton de lancement
bouton_continuer_nombres_joueurs = Button("continuer.png" , position_continuer_nombres_joueurs , 1 )

#bouton d'information sur les régles du jeu
position_bouton_info = (HD[0]- (70+5) , 5 )
bouton_info  = Button("info.png" , position_bouton_info , 1) 

#bouton d'activation et de déactivation du son 
position_bouton_son = (position_bouton_info[0]-(70+15),position_bouton_info[1])
bouton_son  = Button("image_son.png" , position_bouton_son , 1) 


#image principale de l'accueil 
background_img = pygame.image.load('background.png') #image d'arrière plan 
PX = PY = 0

#image principale du jeu 
background_img_jeu = pygame.image.load('table_jeu.png') #image d'arrière plan

# Chargement des images d'icon de son 
son_inactif = pygame.image.load("image_son_mute.png").convert_alpha( ) #image du son inactif  
son_actif = pygame.image.load("image_son.png").convert_alpha() #image du son actif 

#Position du bouton son 
bouton_sonor  = son_actif.get_rect(topleft = position_bouton_son)

#bouton de sortie du jeu 
bouton_sorti  = Button("logout.png" , position_bouton_info , 1)  

#charger la musique et jouer le son 
pygame.mixer.music.load("epicmusicpirate.mp3") #chargement du fichier de son 
pygame.mixer.music.play(loops = -1 , start = 0.0) #boucle infini 
pygame.mixer.music.set_volume(0.5) #réglage du volume de base à 50% 

# État initial de la gestion du son 
statut_son = True
paused = False


# Horloge pour le framerate
clock = pygame.time.Clock()


# État actuel du programme 
etat = "menu"

#time tagger 
show_cursor = True
last_cursor_switch = time.time()
cursor_interval = 0.6  # secondes

#=================================================================================
# SOUS-PROGRAMMES 
#=================================================================================



#fonction image principale 
def positionnement() : 
    ecran.blit(background_img , (PX , PY ))

def positionnement_jeu() : 
    ecran.blit(background_img_jeu , (PX , PY ))
    # ecran.blit(bouton_info , (1110 , 0 ))


#fonction écriture du texte principale "SKULL KING "
def ecriture() : 
    ecran.blit(surbrillance, (80, 290))
    ecran.blit(texte_principale, (75, 285))

def ecriture_jeu () : 
    ecran.blit(surbrillance, (280, 5))
    ecran.blit(texte_principale, (275, 0))

#affichage des boutons de lancement du jeu 
#et des boutons pour l'icon 'INFO' 
def bouton_depart_jouer() : 
    bouton_depart.draws(ecran)
    

def bouton_information_jeu () : 
    bouton_info.draws(ecran)


def bouton_sortie_de_jeu() : 
    bouton_sorti.draws(ecran)


def affiche_carte_individuelle(carte_piocher : int , position_carte_joueur) :
    val_verte = 100
    val_violette = 200
    val_jaune = 300 

    if carte_piocher == 1:
        carte_piocher = carte_noire_1

    elif carte_piocher == 2:
        carte_piocher = carte_noire_2

    elif carte_piocher == 3:
        carte_piocher = carte_noire_3

    elif carte_piocher == 4:
        carte_piocher = carte_noire_4

    elif carte_piocher == 5:
        carte_piocher = carte_noire_5

    elif carte_piocher == 6:
        carte_piocher = carte_noire_6

    elif carte_piocher == 7:
        carte_piocher = carte_noire_7

    elif carte_piocher == 8:
        carte_piocher = carte_noire_8

    elif carte_piocher == 9:
        carte_piocher = carte_noire_9

    elif carte_piocher == 10:
        carte_piocher = carte_noire_10

    elif carte_piocher == 11:
        carte_piocher = carte_noire_11

    elif carte_piocher == 12:
        carte_piocher = carte_noire_12

    elif carte_piocher == 13:
        carte_piocher = carte_noire_13

    elif carte_piocher == 14:
        carte_piocher = carte_noire_14


    elif carte_piocher == 1+ val_verte:
        carte_piocher = carte_verte_1

    elif carte_piocher == 2 + val_verte:
        carte_piocher = carte_verte_2

    elif carte_piocher == 3 + val_verte:
        carte_piocher = carte_verte_3

    elif carte_piocher == 4 + val_verte:
        carte_piocher = carte_verte_4

    elif carte_piocher == 5 + val_verte: 
        carte_piocher = carte_verte_5

    elif carte_piocher == 6  + val_verte:
        carte_piocher = carte_verte_6

    elif carte_piocher == 7 + val_verte: 
        carte_piocher = carte_verte_7

    elif carte_piocher == 8 + val_verte:
        carte_piocher = carte_verte_8

    elif carte_piocher == 9 + val_verte:
        carte_piocher = carte_verte_9

    elif carte_piocher == 10 + val_verte:
        carte_piocher = carte_verte_10

    elif carte_piocher == 11 + val_verte:
        carte_piocher = carte_verte_11

    elif carte_piocher == 12 + val_verte:
        carte_piocher = carte_verte_12

    elif carte_piocher == 13 + val_verte:
        carte_piocher = carte_verte_13

    elif carte_piocher == 14 + val_verte:
        carte_piocher = carte_verte_14




    elif carte_piocher == 1 + val_violette : 
        carte_piocher = carte_violette_1

    elif carte_piocher == 2 + val_violette : 
        carte_piocher = carte_violette_2

    elif carte_piocher == 3 + val_violette : 
        carte_piocher = carte_violette_3

    elif carte_piocher == 4 + val_violette : 
        carte_piocher = carte_violette_4

    elif carte_piocher == 5 + val_violette : 
        carte_piocher = carte_violette_5

    elif carte_piocher == 6 + val_violette : 
        carte_piocher = carte_violette_6

    elif carte_piocher == 7 + val_violette : 
        carte_piocher = carte_violette_7

    elif carte_piocher == 8 + val_violette : 
        carte_piocher = carte_violette_8

    elif carte_piocher == 9 + val_violette : 
        carte_piocher = carte_violette_9

    elif carte_piocher == 10 + val_violette : 
        carte_piocher = carte_violette_10

    elif carte_piocher == 11 + val_violette : 
        carte_piocher = carte_violette_11

    elif carte_piocher == 12 + val_violette : 
        carte_piocher = carte_violette_12

    elif carte_piocher == 13 + val_violette : 
        carte_piocher = carte_violette_13

    elif carte_piocher == 14 + val_violette : 
        carte_piocher = carte_violette_14



    elif carte_piocher == 1 + val_jaune : 
        carte_piocher = carte_jaune_1

    elif carte_piocher == 2  + val_jaune : 
        carte_piocher = carte_jaune_2

    elif carte_piocher == 3 + val_jaune : 
        carte_piocher = carte_jaune_3

    elif carte_piocher == 4 + val_jaune : 
        carte_piocher = carte_jaune_4

    elif carte_piocher == 5 + val_jaune : 
        carte_piocher = carte_jaune_5

    elif carte_piocher == 6 + val_jaune : 
        carte_piocher = carte_jaune_6

    elif carte_piocher == 7 + val_jaune : 
        carte_piocher = carte_jaune_7

    elif carte_piocher == 8 + val_jaune : 
        carte_piocher = carte_jaune_8

    elif carte_piocher == 9 + val_jaune : 
        carte_piocher = carte_jaune_9

    elif carte_piocher == 10 + val_jaune : 
        carte_piocher = carte_jaune_10

    elif carte_piocher == 11 + val_jaune : 
        carte_piocher = carte_jaune_11

    elif carte_piocher == 12 + val_jaune : 
        carte_piocher = carte_jaune_12

    elif carte_piocher == 13 + val_jaune : 
        carte_piocher = carte_jaune_13

    elif carte_piocher == 14 + val_jaune : 
        carte_piocher = carte_jaune_14

    elif carte_piocher == 401 or carte_piocher == 402 or carte_piocher == 403 or carte_piocher == 404 or carte_piocher == 405 : 
        carte_piocher = carte_pirate
    
    elif carte_piocher == 601 or carte_piocher == 602 or carte_piocher == 603 or carte_piocher == 604 or carte_piocher == 605 :
        carte_piocher = carte_fuite 

    elif carte_piocher == 700 :
        carte_piocher = carte_tigresse

    elif carte_piocher == 501 :
        carte_piocher = carte_sirene_1
    
    elif carte_piocher == 502 :
        carte_piocher = carte_sirene_2

    elif carte_piocher == 999 :
        carte_piocher = carte_sk
    ecran.blit(carte_piocher , position_carte_joueur)

def affichage_manche (num_manche : str ) : 
    texte_manche = font_sking.render("MANCHE " + num_manche , True, couleur_blanche) #blanc  
    surbrillance_manche = font_sking.render("MANCHE " + num_manche , True, couleur_noire ) #rouge 
    ecran.blit(surbrillance_manche, (80, 290))
    ecran.blit(texte_manche, (75, 285))


pile_de_carte = pygame.image.load('pile_carte.png') #chargement de l'image de pile de carte 
x_pile_de_carte , y_pile_de_carte = 0 , 420 
def affichage_pile_de_cartes () : 
    ecran.blit(pile_de_carte , (x_pile_de_carte ,y_pile_de_carte ))


x_dos_carte , y_dos_carte = 600 , 30 
def affichage_dos_carte() : 
    ecran.blit(dos_carte , (x_dos_carte , y_dos_carte ))
 
def sauvegarde_joueur (ok , manche ) -> int :
    r = True 
    while r : 
        bal = CD.man(ok, manche)
        r = False 
    return bal

# def sauvegarde_ia () -> int :
#     r = True 
#     while r : 
#         bal = CD.man_ia()
#         r = False 
#     return bal

# Timer
debut_affichage = pygame.time.get_ticks()
afficher_message = True

bool_affichage_vainqueur_tour = True 

def affichage_mise_IA () : 
    temps_actuel = pygame.time.get_ticks()
    for i in range (1,CD.nb_joueurs) :
        result = " a misé "
        texte_surface = police.render((str(CD.tab_j[i])+result+str(CD.mise_automatique (CD.tab_j[i],manche_actuelle,CD.mains[i],i))),True,(255,255,255))  # Blanc
        lokki = texte_surface.get_rect(center=(1000, hauteur // 2))
        # Créer un fond gris derrière le texte
        padding = 20
        fond_rect = pygame.Rect(
            lokki.left - padding,
            lokki.top - padding,
            lokki.width + 2 * padding,
            lokki.height + 2 * padding
            )
        if temps_actuel - debut_affichage < 20000:
            # Dessiner le fond gris derrière le texte
            pygame.draw.rect(ecran, (50, 50, 50), fond_rect, border_radius=10)
            # Dessiner le texte
            ecran.blit(texte_surface, lokki)
        else:
            afficher_message = False



def choisir_carte_joueur_manche_1 (main_perso : list ) :
    d = CD.mains[0][0]
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
            main_perso.remove(CD.mains[0][0])
            #print (f'carte(s) restante(s) dans la main : {mains}')
            CD.recup_cartes(d) 
            return d

        else : 
            d = 401 
            main_perso.remove(d)
            #print (f'carte(s) restante(s) dans la main : {mains}')
            CD.recup_cartes(d)
            return d
    main_perso.remove(d)
    #print(f'carte(s) restante(s) dans la main : {mains}') 
    CD.recup_cartes(d) 
    return d



def choisir_carte_ia_manche_1 (main_perso : list ) :
    d = CD.mains[1][0]
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
            main_perso.remove(d)
            #print (f'carte(s) restante(s) dans la main : {mains}')
            CD.recup_cartes(d) 
            return d

        else : 
            d = 401 
            main_perso.remove(d)
            #print (f'carte(s) restante(s) dans la main : {mains}')
            CD.recup_cartes(d)
            return d
    main_perso.remove(d)
    #print(f'carte(s) restante(s) dans la main : {mains}') 
    CD.recup_cartes(d) 
    return d


bool_vain = True
def affichage_vainqueur_tour  () : 
    global bool_vain
    temps_actuel = pygame.time.get_ticks()
    for i in range (1 , CD.nb_joueurs) :
         

        result = " a gagné le tour "
        #print(f" La carte la plus forte : {CD.comparaison()}")
        indices = [i for i , x in enumerate(CD.depot) if x == CD.comparaison()]
        # print(indices)
        vainqueur_tour = CD.tab_j[indices[0]]
        CD.fu = np.concatenate ((CD.fu , CD.depot))
        #print (vainqueur_tour) 
        while bool_vain : 
            CD.nombre_de_tours_gagné(CD.dico_tg,CD.tab_j[indices[0]])
            bool_vain = False 

        texte_surface = police.render(((str(vainqueur_tour)+result)), True, (255, 255, 255))  # Blanc
        lokki = texte_surface.get_rect(topleft=(350, 700))
        # Créer un fond gris derrière le texte
        padding = 20
        fond_rect = pygame.Rect(
            lokki.left - padding,
            lokki.top - padding,
            lokki.width + 2 * padding,
            lokki.height + 2 * padding
            )
        if temps_actuel - debut_affichage < 30000:
            # Dessiner le fond gris derrière le texte
            pygame.draw.rect(ecran, (50, 50, 50), fond_rect, border_radius=10)
            # Dessiner le texte
            ecran.blit(texte_surface, lokki)
        else:
            bool_affichage_vainqueur_tour = False 



position_bouton_mise = (900,550)
bouton_miser = Button("bouton_miser.png" , position_bouton_mise , 1)

def bouton_mise () :
    bouton_miser.draws(ecran)

position_bouton_manche_suivante = (850 , 490 )
charger_bouton_manche_suivante  = Button("bouton_manche_suivante.png" , position_bouton_manche_suivante , 1 )
def bouton_manche_suivante ():
    charger_bouton_manche_suivante.draws(ecran)


ecriture_manche_actuelle  = font_ecriture.render("MANCHE "+str(manche_actuelle), True, couleur_noire) #blanc  
surbrillance_ecriture_manche_actuelle  = font_ecriture.render("MANCHE "+str(manche_actuelle), True, couleur_or ) #rouge
def affichage_manche_actuelle () : 
    ecran.blit(surbrillance_ecriture_manche_actuelle, (5, 5))
    ecran.blit(ecriture_manche_actuelle, (0, 0))



# Texte saisi par l'utilisateur
active = True  # Activer la saisie
input_text = '' # le texte entré par l'utilisateur 

#=================================================================================
# BOUCLE PRINCIPALE  
#=================================================================================
vitesse_y = -1.2 # Vers le haut (car l'origine est en haut à gauche)

# Position cible (centre de l'écran)
x_carte_joueur , y_carte_joueur = 350 , 470 
y_cible = 270
en_mouvement = True
en_mouvement_dos_carte = True 

largeur, hauteur = 1200, 800


police = pygame.font.Font(None, 60)

for tour in range(manche_actuelle):
    for i in range (CD.nb_joueurs) : 
        if i == 0 : 
            choisir_carte_joueur_manche_1(CD.mains[i])
        else : 
            CD.choisir_cartes_automatique(CD.dico_j ,CD.dico_tg , CD.mains[i][0] , CD.depot , CD.mains[i][0]  , i  )



#boucle de maintient de la fenêtre 
while fixeur:
    ecran.fill(couleur_noire)
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

        # Mise à jour du curseur clignotant
    if time.time() - last_cursor_switch > cursor_interval:
        show_cursor = not show_cursor
        last_cursor_switch = time.time()

    for event in pygame.event.get():

        # déactivation du fixeur 
        if event.type == pygame.QUIT:
            fixeur = False

        #partie son 
        elif event.type == pygame.MOUSEBUTTONDOWN and bouton_sonor.collidepoint(event.pos):
            if statut_son:
                pygame.mixer.music.pause()
                paused = True
                statut_son = False
            else:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    statut_son = True

        #partie changement des menus grâce aux différents boutons 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu" and bouton_depart.est_presser():
                etat = "nombre_joueurs"

            #passer dans le menu pour avoir les infos sur le jeu 
            elif  etat == "menu" and bouton_info.est_presser() :
                etat = "info"  

            elif etat == "ecran_jeu_deux_joueurs" and bouton_miser.est_presser():
                etat = "mise_joueur"

            elif etat == "ecran_jeu_deux_joueurs_apres_mise"  and charger_bouton_manche_suivante.est_presser() and manche_actuelle ==  1:
                manche_actuelle +=1 
                CD.depot.clear()


        #évènement lié à l'état nombre de joueurs 
        elif event.type == pygame.KEYDOWN and etat == "nombre_joueurs": 
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    val = int(input_text)
                    if 2 <= val <= 6:
                        CD.nb_joueurs = int(input_text)

                        sauvegarde_carte = sauvegarde_joueur(CD.nb_joueurs , manche_actuelle )

                        print(f'Texte enregistré dans le module externe : "{CD.nb_joueurs}"')
                        input_text = ""  # Réinitialise si besoin
                        etat = "noms_joueurs"  # ✅ Passe à l'écran suivant
                    else:
                        print("⚠️ Entrez un entier entre 2 et 6")
                else:
                    print("⚠️ Veuillez entrer uniquement un nombre.")
            elif event.unicode.isdigit() and len(input_text) < 3:
                input_text += event.unicode

        #évènement lié à l'état nombre de manches du jeu 
        elif event.type == pygame.KEYDOWN and etat == "nombre_de_manches" :
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    val = int(input_text)
                    if 3 <= val <= 10:
                        CD.nb_manche = input_text
                        print(f'Texte enregistré dans le module externe : "{CD.nb_manche}"')
                        if int(CD.nb_joueurs) == 2 : 
                            etat = "ecran_jeu_deux_joueurs" 
                            input_text = ""  # Réinitialise si besoin
                    else:
                        print("Entrez un nombre  entre 3 et 10")
                else:
                    print("Veuillez entrer uniquement un nombre.")
            elif event.unicode.isdigit() and len(input_text) < 3:
                input_text += event.unicode

        
        #évenement lié aux zones de saisies 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if zone_saisie_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        #évènement de l'état d'information sur le jeu dispo sur la page accueil unqiement 
        elif etat == "info":
            if event.type == pygame.KEYDOWN and bouton_info.est_presser():
                if event.key == pygame.K_DOWN:
                    scroll_y -= 20
                if event.key == pygame.K_UP:
                    scroll_y += 20
                if event.key == pygame.K_ESCAPE:
                    etat = "menu"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # molette haut
                    scroll_y += 20
                elif event.button == 5:  # molette bas
                    scroll_y -= 20


        #évènement lié à l'état de saisie du nom du joueur humain 
        elif event.type == pygame.KEYDOWN and etat == "noms_joueurs":

            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text.strip() != "":
                    # Tu peux ajouter ici le traitement du nom (par exemple l'ajouter à une liste)
                    print(f'Nom saisi : {input_text}')
                    CD.tab_j.append(input_text)
                    CD.ajout_IA()
                    CD.init_dico(CD.dico_tg , CD.dico_j)
                    # CD.init_joueurs()
                    input_text = ""  # Réinitialise si besoin
                    etat = "nombre_de_manches"  # ✅ Passe à l'écran suivant
                else:
                    print("Le nom ne peut pas être vide.")
            elif event.unicode.isalnum() and len(input_text) < 12:
                input_text += event.unicode
        
        #évènement lié à la mise manuelle du joueur humain 
        elif event.type == pygame.KEYDOWN and etat == "mise_joueur":
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    val = int(input_text)
                    if 0 <= val <= manche_actuelle:

                        CD.dico_j[CD.tab_j[0]] = int(input_text) 
                        CD.mise_joueur  = int(input_text)

                        # print(f'Texte enregistré dans le module externe : "{CD.mise_joueur}"')
                        # print(CD.dico_j[CD.tab_j[0]])

                        for i in range (1,len(CD.tab_j)) :
                            CD.mise_automatique (CD.tab_j[i] ,manche_actuelle , CD.mains[i]  , i )


                        input_text = ""  # Réinitialise si besoin
                        etat = "ecran_jeu_deux_joueurs_apres_mise"  # ✅ Passe à l'écran suivant
                    else:
                        print("Entrez un entier compris entre 0 et le nombre de manche ")
                else:
                    print("Veuillez entrer uniquement un nombre.")
            elif event.unicode.isdigit() and len(input_text) < 3:
                input_text += event.unicode

        #elif event.type == pygame.KEYDOWN and etat == "ecran_jeu_deux_joueurs_apres_mise" and manche_actuelle == 1 :
        #    manche_actuelle +=1 
        #     # for tour in range(manche_actuelle):
        #     #     for i in range (CD.nb_joueurs) : 
        #     #         if i == 0 : 
        #     #             choisir_carte_joueur_manche_1(CD.mains[i])
        #     #         else : 
        #     #             CD.choisir_cartes_automatique(CD.dico_j ,CD.dico_tg , CD.mains[i][0] , CD.depot , CD.mains[i][0]  , i  )

        #     while one_tour : 
        #                 for tour in range(manche_actuelle):
        #                     for i in range (CD.nb_joueurs) : 
        #                         if i == 0 : 
        #                             choisir_carte_joueur_manche_1(CD.mains[i])
        #                         else : 
        #                             choisir_carte_ia_manche_1 (CD.mains[i])
        #                             #CD.choisir_cartes_automatique(CD.dico_j ,CD.dico_tg , CD.mains[i][0] , CD.depot , CD.mains[i][0]  , i  )
        #                 one_tour = False


             
            



    if etat == "menu":
        positionnement()
        ecriture()
        bouton_depart_jouer()
        bouton_information_jeu()
        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)

    elif etat == "nombre_joueurs":

        # Dessin du cadre doré
        background_demande  = pygame.image.load('back.png' )
        ecran.blit(background_demande , (PX , PY ))
        question = font_ecriture.render("Entrez le nombre de joueurs entre 2 et 6 ", True, couleur_or)
        ecran.blit(question, question.get_rect(topleft=(35, 200)))
        text_surface = font_ecriture.render(input_text, True, couleur_blanche)
        ecran.blit(text_surface, text_surface.get_rect(topleft=(600-30, 400-25)))

        # # Remplir le rectangle avec une couleur de fond (ex: blanc cassé) 
        pygame.draw.rect(ecran, (170, 170, 170), (590-30, 400-25, 120, 100), border_radius=10)
        pygame.draw.rect(ecran, couleur_or, (590-30, 400-25, 120, 100), 4, border_radius=10)

        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)
        bouton_sortie_de_jeu () 

        display_text = input_text
        if show_cursor:
            display_text += "|"
            surface_texte = font_ecriture.render(display_text, True, (0, 0, 0))
            ecran.blit(surface_texte, (565, 360+7))


    elif etat == "info":
        ecran.fill(couleur_noire)

        # Cadre gris centré dans la grande fenêtre
        cadre_x, cadre_y = (HD[0] - 800) // 2, (HD[1] - 600) // 2
        pygame.draw.rect(ecran, couleur_grise, (cadre_x, cadre_y, 800, 600), border_radius=20)

        # Surface de texte défilable
        surface_texte = font_ecriture.render("texte_info", True, couleur_blanche)
        hauteur_texte = surface_texte.get_height()
        
        # Clipping
        surface_affichage = pygame.Surface((800, 600))
        surface_affichage.fill(couleur_grise)
        surface_affichage.blit(surface_texte, (10, scroll_y))
        
        # Affichage final
        ecran.blit(surface_affichage, (cadre_x, cadre_y))

        # Instructions
        infos_texte = font_ecriture.render("Utilise ↑ ↓ pour défiler, ESC pour revenir", True, couleur_blanche)
        ecran.blit(infos_texte, (HD[0] // 2 - infos_texte.get_width() // 2, cadre_y + 610))

        # Gestion des touches
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scroll_y -= 20
            elif event.key == pygame.K_UP:
                scroll_y += 20
            elif event.key == pygame.K_ESCAPE:
                etat = "menu"

    elif etat == "noms_joueurs":

    # Dessin du cadre doré

        background_demande  = pygame.image.load('back.png' )
        ecran.blit(background_demande , (PX , PY ))
        question = font_ecriture.render("Entrez le nom du joueur humain  ", True, couleur_or)
        ecran.blit(question, question.get_rect(topleft=(35, 200)))
        # text_surface = font_ecriture.render(input_text, True, couleur_blanche)
        ecran.blit(text_surface, text_surface.get_rect(topleft=(600-30, 400-25)))

        # # Remplir le rectangle avec une couleur de fond (ex: blanc cassé) 
        pygame.draw.rect(ecran, (170, 170, 170), (590-150, 400-25, 400, 120), border_radius=10)
        pygame.draw.rect(ecran, couleur_or, (590-150, 400-25, 400, 120), 4, border_radius=10)

        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)
        bouton_sortie_de_jeu ()

        display_text = input_text
        if show_cursor:
            display_text += "|"
            surface_texte = font_ecriture.render(display_text, True, (0, 0, 0))
            ecran.blit(surface_texte, (590-140, 400-25))



    elif etat == "nombre_de_manches":

        # Dessin du cadre doré

        background_demande  = pygame.image.load('back.png' )
        ecran.blit(background_demande , (PX , PY ))
        question = font_ecriture.render("Entrez le nombre de manches entre 3 et 10 ", True, couleur_or)
        ecran.blit(question, question.get_rect(topleft=(35, 200)))
        ecran.blit(text_surface, text_surface.get_rect(topleft=(600-30, 400-25)))

        # # Remplir le rectangle avec une couleur de fond (ex: blanc cassé) 
        pygame.draw.rect(ecran, (170, 170, 170), (590-30, 400-25, 120, 100), border_radius=10)
        pygame.draw.rect(ecran, couleur_or, (590-30, 400-25, 120, 100), 4, border_radius=10)

        bouton_sortie_de_jeu ()
        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)

        display_text = input_text
        if show_cursor:
            display_text += "|"
            surface_texte = font_ecriture.render(display_text, True, (0, 0, 0))
            ecran.blit(surface_texte, (565, 360+7))

    elif etat == "ecran_jeu_deux_joueurs":
        position_carte_joueur = (PX+350 , PY+470 )
        positionnement_jeu()
        affichage_manche_actuelle()
        affichage_dos_carte()

        bouton_sortie_de_jeu ()
        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)

        for manche in range(1,int(CD.nb_manche) +1): 
            # if manche ==1  : 
            affiche_carte_individuelle(sauvegarde_carte , position_carte_joueur)

            # position_carte_joueur[0] = position_carte_joueur[0] + ((manche-1) * 40 )
            # affiche_carte_individuelle(sauvegarde_carte , position_carte_joueur)
        bouton_mise()

    elif etat == "ecran_jeu_deux_joueurs_apres_mise":

        
        positionnement_jeu()
        affichage_manche_actuelle()
        affichage_dos_carte()

        # affichage_pile_de_cartes()

        bouton_sortie_de_jeu ()
        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)

        for manche in range(1,int(CD.nb_manche) +1): 
            if manche_actuelle == 1  :
                
                position_carte_joueur = (x_carte_joueur ,y_carte_joueur )
                
                affiche_carte_individuelle(sauvegarde_carte , position_carte_joueur)

                if afficher_message:
                    affichage_mise_IA()
                
                # elif afficher_message == False : 
                #     if en_mouvement:
                y_carte_joueur+= vitesse_y
                if y_carte_joueur <= y_cible:
                    y_carte_joueur = y_cible
                    en_mouvement = False  # Arrêter le mouvement

                y_dos_carte+= vitesse_y*(-1)
                if y_dos_carte >= y_cible:
                    y_dos_carte = y_cible
                    en_mouvement_dos_carte = False  # Arrêter le mouvement
                

                if en_mouvement_dos_carte == False and one_tour == False : 
                    affiche_carte_individuelle(CD.depot[1], (x_dos_carte,y_dos_carte))

                if bool_affichage_vainqueur_tour and en_mouvement_dos_carte == False : 

                    while one_tour : 
                        for tour in range(manche_actuelle):
                            for i in range (CD.nb_joueurs) : 
                                if i == 0 : 
                                    choisir_carte_joueur_manche_1(CD.mains[i])
                                else : 
                                    choisir_carte_ia_manche_1 (CD.mains[i])
                                    #CD.choisir_cartes_automatique(CD.dico_j ,CD.dico_tg , CD.mains[i][0] , CD.depot , CD.mains[i][0]  , i  )
                        one_tour = False 
                    affichage_vainqueur_tour()
                    bouton_manche_suivante ()
            else : 

                for tour in range (manche_actuelle) :             
                    position_carte_joueur = (x_carte_joueur ,y_carte_joueur )
                    bouton_manche_suivante()
                    for i in range (manche_actuelle) : 
                        x_carte_joueur = x_carte_joueur + (i *40 )
                        affiche_carte_individuelle(sauvegarde_carte , (x_carte_joueur , y_carte_joueur))

                # if afficher_message:
                #     affichage_mise_IA()
                
                # # elif afficher_message == False : 
                # #     if en_mouvement:
                # y_carte_joueur+= vitesse_y
                # if y_carte_joueur <= y_cible:
                #     y_carte_joueur = y_cible
                #     en_mouvement = False  # Arrêter le mouvement

                # y_dos_carte+= vitesse_y*(-1)
                # if y_dos_carte >= y_cible:
                #     y_dos_carte = y_cible
                #     en_mouvement_dos_carte = False  # Arrêter le mouvement
                

                # if en_mouvement_dos_carte == False and one_tour == False : 
                #     affiche_carte_individuelle(CD.depot[1], (x_dos_carte,y_dos_carte))

                # if bool_affichage_vainqueur_tour and en_mouvement_dos_carte == False : 

                #     while one_tour : 
                #         for tour in range(manche_actuelle):
                #             for i in range (CD.nb_joueurs) : 
                #                 if i == 0 : 
                #                     choisir_carte_joueur_manche_1(CD.mains[i])
                #                 else : 
                #                     choisir_carte_ia_manche_1 (CD.mains[i])
                #                     #CD.choisir_cartes_automatique(CD.dico_j ,CD.dico_tg , CD.mains[i][0] , CD.depot , CD.mains[i][0]  , i  )
                #         one_tour = False 
                #     affichage_vainqueur_tour()
                #     bouton_manche_suivante ()    



                

            
            

        

    elif etat == "mise_joueur" : 

        # Dessin du cadre doré
        background_demande  = pygame.image.load('back.png' )
        ecran.blit(background_demande , (PX , PY))
        question = font_ecriture.render("Entrez votre mise : ", True, couleur_or)
        ecran.blit(question, question.get_rect(topleft=(335, 200)))
        ecran.blit(text_surface, text_surface.get_rect(topleft=(600-30, 400-25)))

        # # Remplir le rectangle avec une couleur de fond (ex: blanc cassé) 
        pygame.draw.rect(ecran, (170, 170, 170), (590-30, 400-25, 120, 100), border_radius=10)
        pygame.draw.rect(ecran, couleur_or, (590-30, 400-25, 120, 100), 4, border_radius=10)

        bouton_sortie_de_jeu ()
        ecran.blit(son_actif if statut_son else son_inactif, bouton_sonor)

        display_text = input_text
        if show_cursor:
            display_text += "|"
            surface_texte = font_ecriture.render(display_text, True, (0, 0, 0))
            ecran.blit(surface_texte, (565, 360+7))
    pygame.display.update()

#=================================================================================
# FIN DU JEU  
#=================================================================================

#fin du jeu / fonction quit()
pygame.mixer.music.stop()
pygame.quit()


