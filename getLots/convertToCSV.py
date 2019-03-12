# coding: utf-8

# ConvertToCSV
# Auteur: Raphaël Marquis-Pelletier
#
# Utilisation:
# convertToCSV.py -i fichierInput.html

from sys import argv
from bs4 import BeautifulSoup
import re
from slugify import slugify
from dateutil import parser
import unicodecsv as csv

inputhtml = argv[2]
soup = BeautifulSoup(open(inputhtml), 'html.parser')

devisesDict = {
'€':'EUR',
'$':'USD',
'£':'GBP'
}

def getEncan():
    return "Christies"

def getTitreVente():
    if maison == 'Christies':
        return soup.find('ul', id="sale_info_container").find('h2', class_="browse-sale-title").string.lstrip()

def getDateVente():
    if maison == 'Christies':
        dateEtLieux = soup.find('ul', id="sale_info_container").find('span', class_="sale-date").string
        date = parser.parse(re.search('(.+),', dateEtLieux).group(1).lstrip()).strftime("%Y-%m-%d")
        return date
def getLieuVente():
    if maison == 'Christies':
        dateEtLieux = soup.find('ul', id="sale_info_container").find('span', class_="sale-date").string
        lieu = re.split(",", dateEtLieux)[1].lstrip().rstrip()
        return lieu

maison = getEncan()
titreVente = getTitreVente()
dateVente = getDateVente()
lieu = getLieuVente()

csvFilename = maison + "_" + dateVente + "_" + lieu + "_" + slugify(titreVente) + ".csv"

print(csvFilename)

lots = []
objets_rejetes = []

for lot in soup.find_all('tr'):
    try: #Essaie de lire chaque lot

        # 1  - Déterminer le numéro de lot
        try:
            numeroLot = lot.find('td', class_='lot-info').find('span', class_='lot-number').string
            pass
        except Exception as e:
            raise

        # 2 - Determiner l'Artiste
        try:
            artisteData = lot.find('td', class_='lot-info').find('span', class_='lot-description').string
            artiste = artisteData.replace((re.search('(\(.+\))', artisteData).group(1)), '').rstrip()
            pass
        except Exception as e:
            raise

        # 3 - Determiner le titre de l'oeuvre
        try:
            titre = lot.find('td', class_='lot-info').find('span', class_='lot-maker').string
            pass
        except Exception as e:
            raise
        # 4 - Determiner le medium
        try:
            medium = lot.find('td', class_='lot-info').find('span', class_='medium-dimensions').contents[0]
            pass
        except Exception as e:
            print('Incapable de déterminer le médium')

        # 5 - Determiner la taille
        try:
            #données brutes de la page web
            dimensionsData = lot.find('td', class_='lot-info').find('span', class_='medium-dimensions').contents[2]

            #on enlève les données en pouces
            #if (lieu == 'Paris'):
            #    dimensionsData =  re.search('(.+)cm', dimensionsData).group(1).rstrip().lstrip()

                #on regarde il y a combien de dimensions
                # le nombre de caractère - le nombre de caractères sans les x  = le nombre de x
            #    xCount = len(dimensionsData) - len(dimensionsData.replace('x', ''))

            #    if (xCount < 3 and xCount > 0):
            #        dimensions = dimensionsData.split(" x ")
            #    else:
            #        dimensions = ['','','']
            #else:
            dimensions = ['12','12','12']

            pass
        except Exception as e:
            print('Impossible de déterminer la taille')


        # 6 - Determiner le titre de l'oeuvre
        try:
            titre = lot.find('td', class_='lot-info').find('span', class_='lot-maker').string
            pass
        except Exception as e:
            raise

        # 7 - Determiner le prix payé et la devise
        try:
            prixRaw = lot.find('td', class_='estimate').find_all('span', class_='lot-description')[1].string.encode('utf-8')
            prix = (re.search('([\d,]+)', prixRaw).group(1)).replace(',', '')

            deviseRaw = prixRaw.replace((re.search('([\d,]+)', prixRaw).group(1)), '').lstrip()

            #À réecrire avec le dictionnaire deviseDict. Ce qui suit est une patch rapide et inefficace
            if (deviseRaw == "€"):
                devise = 'EUR'
            elif (deviseRaw == "£"):
                devise = 'GBP'
            else:
                devise = 'INC'

            pass
        except Exception as e:
            print('Impossible de déterminer le prix')

        dictLot = {
        'Maison':maison,
        'TitreDeLaVente':titreVente,
        'DateVente':dateVente,
        'Lieu': lieu,
        'NumeroDeLot':numeroLot,
        'Artiste':artiste,
        'TitreOeuvre': titre,
        'Medium': medium,
        'X': dimensions[0],
        'Y': dimensions[1],
        'Z': dimensions[2],
        'Prix': prix,
        'Devise': devise
        }
        lots.append(dictLot)
        pass
    except Exception as e: #lots rejetés
        print("Lot rejeté")

with open(csvFilename, 'wb') as csvfile:
    fieldnames = ['Maison','TitreDeLaVente', 'DateVente', 'Lieu','NumeroDeLot', 'Artiste', 'TitreOeuvre', 'Medium', 'X', 'Y', 'Z', 'Prix', 'Devise']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quotechar='"')

    writer.writeheader()

    for lot in lots:
        writer.writerow(lot)
