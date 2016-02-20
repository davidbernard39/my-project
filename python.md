# Python 

[Openclassrooms](https://openclassrooms.com/courses/apprenez-a-programmer-en-python)

## Partie 1 - Introduction à python

### Qu'est ce que python ?

- Langage interprété
- Langage à typage dynamique
- Permet de créer des scripts et toute sorte de programmes (jeux, logiciels, progiciels...)
- Peut être étendu avec des bibliothèques
- Portable sous différents OS

### Interpréteur de commandes

- Permet de tester du code
- Permet de faire des calculs (approximation avec les nombres décimaux)

### Les variables

Types de données :
- int
- float
- str (chaine de caractères)
- bool (True; False)

entre guillemets "chaine"
entre apostrophes 'chaine'
entre triples guillemets """chaine""" (les sauts de lignes sont transformés en \n)

Permuter deux variables : a,b = b,a

Fonctions :
- type(var) : affiche le type de la variable
- print(var) : affiche la valeur de la variable
- input(var) : demande saisie utilisateur (affiche le contenu de var)

### Les structures conditionnelles

if predicat:
    # instruction
elif predicat:
    # instruction
else:
    # instruction
    
Opérateurs logiques : and, or, not

### Les boucles

while condition:
    # instruction

for element in sequence:
    # instruction
    
break; continue

### Modularité (1/2)

#### Fonctions

- Créer une fonction :

def nom_de_la_fonction(param1, param2, paramN):
    # instructions

- Valeur par défaut d'un paramètre :

def nom_de_la_fonction(param=valDef):
    # instructions 
    
- Commentaire entete de fonction (docString) :

def nom_de_la_fonction():
    """ Doc
    DocString
    """

- Passage de paramètre via le nom :

def nom_de_la_fonction(a=1,b=2,c=3):
nom_de_la_fonction(b=9)

- Signature d'une fonction : son nom. On ne peut pas surcharger une fonction en python.

- Return

def nom_de_la_fonction():
    return valeur

#### Fonctions lambda

f = lambda x: x * x

#### Modules

import math [as name_space]

math.sqrt(16)
name_space.sqrt(16)

from math import sqrt [as racine]

### Modularité (2/2)

Créer un script exécutable / module :

```
    #!/usr/bin/python
    #-*-coding:utf-8 -*
    
    """" Commentaire de module """"
    
    def fonction:
        """ Commentaire de fonction """
        # instruction
```

Dans le même répertoire importer son module :

from mon_module import *

Le nom du module ne doit pas commencer par un chiffre et ne doit pas contenir de '-'

Tests directement dans le module :

if __name__ == "__main__":

Permet de tester si le fichier appelé est le fichier exécuté.

- Module : permet de regrouper des fonctions
- Package : permet de regrouper des modules

Packages = répertoire 

importer un package : import nom_bibliotheque
accéder à un sous package : import nom_bibliotheque.sous_package

fichier d'initialisation d'un package : __init.py__

### Les exceptions

Forme minimale :

try:
    # instruction
except:
    # catch
    
Forme complète :

try:
    # instruction
except typeError:
    # catch typeError
    
try:
    # instruction
except typeError as exceptionRetournee:
    # catch typeError (exceptionRetournee)
    
try:
    # instruction
except:
    # catch
else:
    # instruction si pas d'erreur

try:
    # instruction
except:
    # catch
finally:
    # instruction executée si erreur ou non

Le mot clé pass :

try:
    # instruction
except:
    pass # ne rien faire en cas d'exception

- Assertions

assert test

lève une exception AssertionError

```
annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
```

- Lever une exception : raise TypeDeLexception

```
annee = input() # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
```

## Partie 2 - POO côté utilisateur

### Les chaines de caractères

- En python tout est objet. Un objet est composé de variables et de fonctions.
- Les variables sont en réalité des objets
- Les types de données sont des classes

chaine.lower() : passe en minuscule chaine

objet.methode()

chaine = str() <=> chaine = ""

Formatage de chaines :

    nom = "toto"
    print("Hello {0}".format(nom))

Formatage avec noms de variables :

    adresse = """
    {no_rue}, {nom_rue}
     {code_postal} {nom_ville} ({pays})
    """.format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
    print(adresse)

Concaténation avec + :

    chaine1 + chaine2
    
Accéder aux caractères d'une chaine :

    chaine[i]
    
On peut accéder aux caractères en partant de la fin (chaine[-1])

Longueur d'une chaine : len(chaine)

Sélection de chaine : chaine[0:2]

### Listes et tuples (1/2)

#### Listes

Les listes sont des séquences comme les chaines de caractères qui peuvent contenir n'importe quel type d'objet au lieu de contenir des caractères.

Créer une liste vide :

ma_liste = list()
ma_liste = []

Créer une liste non vide : ma_liste = [1,2,3,4,5]

Accéder à un élément de la liste : ma_liste[i]

Ajouter un élément à la liste : ma_liste.append(var)

Concaténation de liste : ma_liste1 + ma_liste2

Suppression d'élément de liste : 

del var / del ma_liste[i]
ma_liste.remove(var)

Parcours de liste : 

i = 0
while i < len(ma_liste):
	# instruction
	
for element in ma_liste:
	# instruction

for i, element in enumerate(ma_liste):
	# instruction
	
for elt in enumerate(ma_liste): 
	# elt est un tuple (indice, val)
	
#### tuples

Les tuples sont des listes immutables

Créer un tuple vide : t = ()

Créer un tuple non vide : t = (1,) / t = 1, / t = (1,2,5)

Les tuples peuvent être utilisés dans des fonctions pour retourner plusieurs valeurs.

### Listes et tuples (2/2)

#### Listes et chaines

Des chaines aux listes : chaine.split(" ")

Des listes aux chaines : " ".join(tab)

Fonction avec une liste de paramètres variable : def fonc(*params)

Transformer une liste en paramètres de fonctions : 
tab = [1,3]
print(*tab)

#### Compréhensions de liste

- Permettent de modifier / filter une liste

>>> liste=[0,1,2,3,4]
>>> [nb * nb for nb in liste]
[0, 1, 4, 9, 16]


>>> [nb * nb for nb in liste if nb%2 == 0]
[0, 4, 16]


>>> toto=[
...     ("fraises", 7),
...     ("carotte",25)
... ]

>>> tata=[(qtt,nom) for nom,qtt in toto]
>>> sorted(tata)
[(7, 'fraises'), (25, 'carotte')]

La syntaxe pour effectuer un filtrage est la suivante : nouvelle_squence = [element for element in ancienne_squence if condition].

### Dictionnaires

#### Dict

Créer un dictionnaire vide : 
d = dict()
d = {}

Créer un dictionnaire rempli :
d = {cle1:val1,cleN:valN}xxx

Ajouter des éléments :
d[cle] = val

Accéder à un élément :
d[cle]

ex avec cle tuple :
d[a,1] = val

Supprimer un élément :
del d[cle]
d.pop(cle)

On peut mettre des fonctions dans un dictionnaire :
d[cleFonc] = f
d[cleFonc]() equivalent à f()

Parcours des clés :

for c in d.keys()

Parcours des valeurs :

for v in d.values()

Parcours des clés et valeurs :

for c,v in d.items()

Test d'une valeur :

if val in d.values()

Fonction avec une liste de paramètres nommés variable : def fonc(**params)

Transformer une liste en paramètres de fonctions : 
map = {cle:val,cleN:valN}
fonc(**tab)

#### Set

Créer un set :
s = set()
s = {val1,valN}

Ajouter un élément :
s.add(val)




