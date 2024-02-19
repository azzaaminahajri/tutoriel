# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#faire appel au module csv
import csv

# Lecture du fichier CSV dans un DataFrame
data =('C:/Users/Hp/Desktop/nychousing.csv')
# Liste pour stocker le contenu du fichier CSV
contenu_csv = []


# Parcourir le fichier CSV et lire son contenu
with open(data, newline='') as csvfile:
    lecteur_csv = csv.reader(csvfile, delimiter=',')
    for index, ligne in enumerate(lecteur_csv):
        # Ajouter la ligne à la liste avec son numéro d'index
        contenu_csv.append((index, ligne))

# Afficher le contenu de la liste avec la fonction enumerate
for index, ligne in contenu_csv:
    print(f"Index {index}: {ligne}")

