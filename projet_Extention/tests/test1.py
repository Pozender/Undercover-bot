from random import *

# Le tirage au sort de l'undercover
nb_players = int(input("Indiquez le nombre de joueurs: "))
if nb_players < 1:
    while nb_players < 1:
        print("Erreur il ne peut pas y avoir moins de 1 joueur")
        nb_players = int(input("Indiquez le nombre de joueurs: "))
        if nb_players >= 1 :
            break

undercover = randint(1, nb_players)


# Le tirage au sort de mots
second_array = ["proute", "caca"]
third_array = ["Saucisse", "Kebab", "falafel"]
fourth_array = ["Photo", "Vidéo", "dessin"]
first_array = [second_array, third_array, fourth_array]

a = randint(0, len(first_array) - 1)
b = first_array[a]
c = randint(0, len(b) - 1)
word = b[c]
if c == len(b) - 1:
    undercover_word = b[c - 1]
else:
    undercover_word = b[c + 1]
print("The undercover is the player ", undercover)
print("players word = '",word,"'")
print("undercover word = '",undercover_word,"'")