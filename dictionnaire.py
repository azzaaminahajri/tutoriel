# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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


