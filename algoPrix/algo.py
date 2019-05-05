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
from statistics import mean

prixMoyen = {
0: 352.87,
1: 1359.40,
2: 8007.12,
3: 455551.90
}

def getMarche(genre, vivant, decoratif, portee, galerie, musee, revue):
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
    else:
        marche = 1

    return marche

def getPrix(genre, vivant, decoratif, portee, galerie, musee, revue, dimx, dimy, medium):
    aire = dimx * dimy

    #1 déterminer le marché
    marche = getMarche(genre, vivant, decoratif, portee, galerie, musee, revue)

    #2 règles pour chaque marché
    Prix = prixMoyen[marche]

    if (marche == 0):
        prixAire = (0.008648421 * aire) + 80
        Prix = mean([Prix, prixAire])

    if (marche == 1):
        prixAire = (0.1245*(aire^6))-(5.3884*(aire^5))+(89.516*(aire^4))-(715.87*(aire^3))+(2825.6*(aire^2))-(4877,7*aire)+2924
        Prix = mean([Prix, prixAire])

    print('Marché: %s' % (marche))
    return Prix

if __name__ == "__main__":
   genre = int(input('Genre [0=Homme, 1=Autre, 2=Femme] >'))
   vivant = int(input('Vivant [0=Non, 1=Oui] >'))
   decoratif = int(input('Décoratif [0=Non, 1=Oui] >'))
   portee = int(input('Portée [0=Locale, 1=Nationale, 2=Internationale] >'))
   galerie = int(input('Exposé dans une galerie [0=Non, 1=Oui] >'))
   musee = int(input('Musee [0=Non, 1=Oui] >'))
   revue = int(input('Revue [0=Non, 1=Oui] >'))
   dimx = int(input('Dimension en X en cm>'))
   dimy = int(input('Dimension en Y en cm>'))
   medium = int(input('Medium [0=Aquarelle/dessin/seriegraphoe, 1=Autre, 2=Acrylique/huile] >'))

   print(getPrix(genre, vivant, decoratif, portee, galerie, musee, revue, dimx, dimy, medium))
