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

