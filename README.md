# Tutoriel:Qu'est-ce que la fonction enumerate: Pourquoi et comment l'utiliser?
# Introduction
La manipulation de données avec Python est devenue une compétence essentielle dans de nombreux domaines,ce langage de programmation nous permet de réaliser tout le processus de modification ou de transformation des données afin d’en extraire des informations précieuses,ce processus repose souvent sur des concepts clés tels que la création de structures de données, l'indexation, le filtrage, le tri, le regroupement, l'agrégation et la transformation des données.
Python propose la fonction enumerate qui se qualifie comme un outil puissant pour les développeurs,en effet sa principale tâche est de simplifier l'itération et la manipulation d'une séquence tout en conservant son index.
Cette fonction permet de parcourir les données d'une maniére simple à l'inverse de certains langages de programmation où il faut gérer manuellement les indices lors de l'itération sur une structure de données , la fonction enumerate associe chaque élément d'une séquence à son index correspondant,Cette approche permet aux développeurs de traiter les données de manière plus lisible, en évitant les erreurs potentielles liées à la gestion manuelle des indices.
Par exemple dans le développement logiciel cette fonction est précieuse pour traiter les données avec clarté , améliorant ainsi la robustesse et la maintenabilité du code tout en facilitant le travail avec les séquences de données.
# Contexte 

La nécessité de manipuler d'une maniére efficace les données et d'avoir accés à leurs indices s'avére être un élément incontournable,Que ce soit pour le parcours d'une liste d'éléments et l'analyse des ensembles de données ou le traitement des informations structurés,la fonction enumerate met à la dispositon des développeurs une solution efficace et élégante.
L'utilisation appropriée de enumerate renforce la maniére dont on gére des informations et favorise la réalisation des objectifs organisationnels dans un environnement professionnel exigeant.


Afin de mieux découvrir la fonction enumerate nous allons explorer les données d'un fichier csv nommé "New york city housing" et parcourir les éléments de ce fichiers mais sous la forme 
de tout les conteneurs (listes/ensembles/dictionnaires/tuples).
nous allons aussi explorer les situations courantes où la fonction enumerate peut être utile telles que:
(L'itération avec un accès aux index/
La modification d'une séquence pendant l'itération/
L'Affichage des éléments avec leurs indices/
Création d'un dictionnaire à partir d'une liste avec des indices/ 
Comparaison de deux listes avec des indices/
Suppression de certains éléments d'une liste tout en parcourant)

# Connaissances Préalables
 Afin de suivre ce tutoriel,il est important d'avoir des connaissances de base en Python, notamment sur les concepts suivants:
 Les conteneurs sous python.
 Les fonctions en python.
# Premiére utilisation avec enumerate dans les conteneur pythons
Dans cet exemple nous pouvons voir comment parcourir et accéder aux éléments d'un fichier csv en stockant son contenu dans une liste tout en utilisant la fonction enumerate.
afin d'avoir accés au contenu du fichier csv nous devons faire appel au module csv.<br>
Exemple 1 :
```python
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
```
#capture liste 
comme nous le montre la  photo du terminal dans pycharm nous avons parcouru et lu le contenu du fichier csv qu'on a par la suite ajouter dans une liste vide , quant à l'affichage du résultat 
nous pouvons voir que la fonction enumerate  associe chaque élément de la liste à son index correspondant.
Dans l'exemple suivant nous allons reproduire les mêmes étapes qu'on a fait à l'exemple précédent mais à la place des liste nous allons manipuler des ensembles.<br>
Exemple 2 :
```python
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
```
#captureensemble
<br>
Exemple 3:
```python
import csv

# Chemin vers le fichier CSV
data = ('C:/Users/Hp/Desktop/nychousing.csv')
# Créer une liste pour stocker le contenu du fichier CSV sous forme de tuple
contenu_csv = []

# Parcourir le fichier CSV et lire son contenu
with open(data, newline='') as csvfile:
    lecteur_csv = csv.reader(csvfile)
    for index, ligne in enumerate(lecteur_csv):
        # Convertir chaque élément de la ligne en tuple
        tuple_ligne = tuple(ligne)
        # Ajouter le tuple de ligne à la liste avec son numéro d'index
        contenu_csv.append((index, tuple_ligne))

# Afficher le contenu du tuple avec la fonction enumerate
for index, ligne in contenu_csv:
    print(f"Index {index}: {ligne}")
```
Dans cet exemple nous avons parcouru et lu le fichier csv et obtenu son contenu qu'on a stocké dans un tuple qui se définit comme une collection immuables ce qui signifie qu'une fois créés, ils ne peuvent pas être modifiés à l'inverse des ensembles qui sont des collections mutables.
<br>
L'exemple suivant est un peu complexe par rapport au exepmles précédents , en effet dans cet exemple nous allons parcourir un fichier csv et ajouter son contenu dans un dictionnaire par la suite nous allons extraire seulement les données des logements situés dans l'état nommé 'FORREST HILLS' ,grâce à la fonction enumerate nous pouvons accéder à l'indice des lignes du fichiers.
<br>
Exemple 4 :
```python
import pandas as pd

# Lecture du fichier CSV dans un DataFrame
data = pd.read_csv('C:/Users/Hp/Desktop/nychousing.csv')

# Affichage des premières lignes du DataFrame
print(data.head())
print("succés")




dictionnairedata=data.to_dict(orient='records')
print(dictionnairedata)
print(type(dictionnairedata))
for indice, element in enumerate(dictionnairedata):
    #print(f"Indice : {indice}")
    for cle, valeur in element.items():
        #print(f"    key : {cle}, Value : {valeur}")
        for element in dictionnairedata:
            if 'Forest Hills' in element['STATE']:
                print("Indice:", dictionnairedata.index(element))
                for k, v in element.items():
                    print(f"    key : {k}, Value : {v}")
```
comme on peut le voir nous avons installé la bibliothéque pandas qui prend en charge la lecture et l'écriture de données à partir de divers formats de fichiers, notamment CSV, Excel, SQL, HDF5, JSON, HTML etc.. 
vous pouvez installer pandas en exécutant la commande suivante dans le terminal de votre environnement de développement intégré (IDE)
```python
pip install pandas
```





 
 


