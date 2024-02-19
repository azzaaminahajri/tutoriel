import csv
# Définir le chemin vers le fichier CSV
data = ('C:/Users/Hp/Desktop/nychousing.csv')

# Créer un ensemble pour stocker le contenu du fichier CSV
contenu_ensemble= set()

# Parcourir le fichier CSV et lire son contenu
with open(data, newline='') as csvfile:
    lecteur_csv = csv.reader(csvfile)
    for index, ligne in enumerate(lecteur_csv):
        # Ajouter la ligne à l'ensemble
        contenu_ensemble.add((index, tuple(ligne)))

# Afficher le contenu de l'ensemble avec la fonction enumerate
for index, ligne in contenu_ensemble:
    print(f"Index {index}: {ligne}")
