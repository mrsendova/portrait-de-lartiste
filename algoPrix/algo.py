# coding: utf-8
#
#  Algorithme de détermination du prix d'une oeuvre d'art, basé sur une étude
#  statistique menée au préalable à partir de sources variables (encans des
#  maisons Sotheby's et Christie's, visite de galeries montréalaises, profils
#  Artsy de profils de marchés intermédiaires, etc...)
#
#  L'algorithme incorpore également une partie de hasard ainsi qu'une fluctuation
#  liée à la température ambiante.
#
#  À faire: Ajouter une requête à certains indices boursiers.
#
#
#  UTILISATION
#  python algo.py
#




from sys import argv
import math
import random
from statistics import mean

prixMoyen = {
0: 352.87,
1: 1359.40,
2: 8007.12,
3: 455551.90
}

def getMarche(genre, decoratif, portee, galerie, musee, revue):
    # Ajustements
    if (portee == 0 and decoratif == 1):
        musee *= 0.6
        revue *= 0.4
        galerie *= 0.2


    if (decoratif == 1 and (galerie + revue + musee) < 1 and portee == 0):
        # Le tableau d'épicerie
        marche = 0
    elif (decoratif == 0 and (galerie + revue + musee) < 1 and portee == 0):
        # l'étudiant qui sort de l'école
        marche = 1
    elif (decoratif == 0 and 1 <= (galerie + revue + musee) <= 2 and portee <= 1):
        # l'artiste émergent
        marche = 2
    elif ((galerie + revue + musee) > 2 and portee == 2):
        # l'artiste établi internationalement
        marche = 3
    elif ((galerie + revue + musee) == 3 and portee == 1):
        # l'artiste reconnu nationalement
        marche = 2
    else:
        marche = 1

    return marche

def getPrix(genre, decoratif, portee, galerie, musee, revue, dimx, dimy, medium):
    aire = dimx * dimy
    print(aire)

    #1 déterminer le marché
    marche = getMarche(genre, decoratif, portee, galerie, musee, revue)

    #2 règles pour chaque marché
    Prix = prixMoyen[marche]

    if (marche == 0):
        prixAire = (0.008648421 * aire) + 80
        print(prixAire)
        Prix = mean([Prix, prixAire])
        print(Prix)

    if (marche == 1):

        # Aire
        if (aire > 5 and aire < 11000):
            prixAire = ((-3*(10 ** -19))*(aire ** 6))+((8*(10 ** -15)) * (aire ** 5))-((9*(10 ** -11)) * (aire ** 4)) + ((5*(10 ** -7)) * (aire ** 3)) - (0.001 * (aire ** 2))+(1.0572*aire)+4.4567
        else:
            prixAire = (0.0899 * aire) + 1001.2
        print(prixAire)
        Prix = mean([Prix, (prixAire * 0.3)])

        #Genre
        if (genre == 2):
            Prix = Prix * 1.256

        #Medium
        if (medium == 0):
            Prix = Prix * 0.2

        Prix = Prix * (1 - random.uniform(-0.3, 0.3))

        #Mode supernotstar
        if (random.random() > 0.87):
            Prix = Prix * (random.uniform(0.1,0.3))
            print('mode not star')

    if (marche == 2):

        # Aire
        if (aire > 600 and aire < 20000):
            prixAire = ((-4*(10 ** -20))*(aire ** 6))+((3*(10 ** -15)) * (aire ** 5))-((7*(10 ** -11)) * (aire ** 4)) + ((8*(10 ** -7)) * (aire ** 3)) - (0.0049 * (aire ** 2))+(12.993*aire)-5249.2
        else:
            prixAire = (0.8717 * aire) - 4100.3
        Prix = mean([Prix, prixAire])

        #Genre
        if (genre == 2):
            Prix = Prix * 0.6109

        #Medium
        if (medium == 0):
            Prix = Prix * 0.1

    if (marche == 3):

        # Aire
        if (aire > 200 and aire < 5500):
            prixAire = ((5*(10 ** -16))*(aire ** 6))-((9*(10 ** -12)) * (aire ** 5))+((5*(10 ** -8)) * (aire ** 4)) - (0.0001 * (aire ** 3)) + (0.1038 * (aire ** 2))+ (23.539 * aire) + 5598.5
        else:
            prixAire = (0.1852 * aire) + 7381
        Prix = mean([Prix, prixAire])

        #Genre
        if (genre == 2):
            Prix = Prix * 0.6109

        #Medium
        if (medium == 0):
            Prix = Prix * 0.1

        #Mode superstar
        if (random.random() > 0.9):
            print('mode star')
            Prix = Prix * (random.uniform(1,6))


    # On ajoute un peu d'aléatoire
    Prix = Prix * (1 - random.uniform(-0.2, 0.15))
    print('Marché: %s' % (marche))
    print(len(str(round(Prix,2))))
    return round(Prix,2)

if __name__ == "__main__":
    genre = int(argv[1])
    decoratif = int(argv[2])
    portee = int(argv[3])
    galerie = int(argv[4])
    musee = int(argv[5])
    revue = int(argv[6])
    dimx = int(argv[7])
    dimy = int(argv[8])
    medium = int(argv[9])
    print(getPrix(genre, decoratif, portee, galerie, musee, revue, dimx, dimy, medium))
#   decoratif = int(input('Décoratif [0=Non, 1=Oui] >'))
#   portee = int(input('Portée [0=Locale, 1=Nationale, 2=Internationale] >'))
#   galerie = int(input('Exposé dans une galerie [0=Non, 1=Oui] >'))
#   musee = int(input('Musee [0=Non, 1=Oui] >'))
#   revue = int(input('Revue [0=Non, 1=Oui] >'))
#   dimx = int(input('Dimension en X en cm>'))
#   dimy = int(input('Dimension en Y en cm>'))
#   medium = int(input('Medium [0=Aquarelle/dessin/seriegraphoe, 1=Autre, 2=Acrylique/huile] >'))
