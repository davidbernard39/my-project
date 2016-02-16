# Python 

[Openclassrooms](https://openclassrooms.com/courses/apprenez-a-programmer-en-python)

## Partie 1 - Introduction à python

### Qu'est ce que python ?

- Langage interprété
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




