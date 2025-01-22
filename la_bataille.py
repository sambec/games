import random

#Pour donner la valeur des cartes
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi',
'As']
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, \
'9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

# la liste deck qu'on crée juste en dessous en créant les cartes
deck = []

#Pour créer les cartes
for couleur in couleurs:
    for nom in noms:
        deck.append((nom,couleur))

random.shuffle(deck)
# print(deck, len(deck))

#Pour diviser le deck en deux
#C'est de la compéhension de liste le fait de faire une boucle for dans les crochets
#Joueur 1 du coup c'est les cartes indice 0 à 25
#joueur1 = [deck[0], deck[1], ..., deck[25]]
joueur1 = [deck[i] for i in range(26)]
random.shuffle(joueur1)
#joueur2 = [deck[26], deck[27], ..., deck[51]]
# une autre solution : joueur2 = deck[26:]
joueur2 = [deck[i] for i in range(26,52)]
random.shuffle(joueur2)
#pour vérifier que les deux tas de cartes font la même taille:
# print(len(joueur1), len(joueur2))

#ici on initialise les compteurs à zéro pour les points
points_joueur1 = 0
points_joueur2 = 0

#c'est ici que ce joue vraiment la partie, on va tirer les cartes et voir qui gagne dans chaque if
#une première version mais qui ne permet de vider le paquet de carte c'est juste random
# for i in range(26):
#     carte_jouee1 = random.choice(joueur1)
#     carte_jouee2 = random.choice(joueur2)
#     if carte_jouee1[0] > carte_jouee2[0]:
#         print("joueur 1 a gagné")
#         points_joueur1 += 1
#     if carte_jouee2[0] > carte_jouee1[0]:
#         print("joueur 2 a gagné")
#         points_joueur2 += 1
#     else:
#         print("égalité")

print("~~~ Let the game begin ~~~")
#une deuxième version
for i in range(26):
    # Tirer une carte pour chaque joueur (supprime la carte de la main)
    print("-----")
    carte_jouee1 = joueur1.pop(0)  # Retire et retourne la première carte
    print(f"Joueur 1 a joué {carte_jouee1}") #Affiche quelles cartes sont jouées pour vérifier si triche hehe
    carte_jouee2 = joueur2.pop(0)
    print(f"Joueur 2 a joué {carte_jouee2}") 

    # Comparer les valeurs des cartes jouées
    valeur1 = valeurs[carte_jouee1[0]]  # Valeur de la carte joueur 1
    valeur2 = valeurs[carte_jouee2[0]]  # Valeur de la carte joueur 2
    if valeur1 > valeur2:
        print("Joueur 1 gagne ce tour")
        points_joueur1 += 1
    elif valeur2 > valeur1:
        print("Joueur 2 gagne ce tour")
        points_joueur2 += 1
    else:
        # TO DO : trouver un moyen de faire que cette carte soit vraiment remise en jeu au prochain tour 
        print("Égalité, cette carte ce joue au prochain tour")

print("~~~ C'est fini ! ~~~")
#maintenant on va chercher qui a eu le plus de points pour cette partie grâce à la variable points_joueur
if points_joueur1 > points_joueur2:
    print("Bravo joueur 1 a gagné la bataille (mais pas la guerre)")
if points_joueur2 > points_joueur1:
    print("Bravo joueur 2 a gagné la bataille (mais pas la guerre)")
if points_joueur1 == points_joueur2:
    print("Egalité on recommence on peut pas en rester là")

