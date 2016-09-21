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
- `int`
- `float`
- `str` (chaine de caractères)
- `bool` (True; False)

entre guillemets "chaine"
entre apostrophes 'chaine'
entre triples guillemets """chaine""" (les sauts de lignes sont transformés en \n)

Permuter deux variables : `a,b = b,a`

Fonctions :
- `type(var)` : affiche le type de la variable
- `print(var)` : affiche la valeur de la variable
- `input(var)` : demande saisie utilisateur (affiche le contenu de var)

### Les structures conditionnelles

```
if predicat:
    # instruction
elif predicat:
    # instruction
else:
    # instruction
```     
Opérateurs logiques : `and`, `or`, `not`

### Les boucles

```
while condition:
    # instruction
```
```
for element in sequence:
    # instruction
```

`break`; `continue`

### Modularité (1/2)

#### Fonctions

- Créer une fonction :

```
def nom_de_la_fonction(param1, param2, paramN):
    # instructions
```

- Valeur par défaut d'un paramètre :

```
def nom_de_la_fonction(param=valDef):
    # instructions
```

- Commentaire entete de fonction (docString) :

```
def nom_de_la_fonction():
    """ Doc
    DocString
    """
```

- Passage de paramètre via le nom :

```
def nom_de_la_fonction(a=1,b=2,c=3):
nom_de_la_fonction(b=9)
```

- Signature d'une fonction : son nom. On ne peut pas surcharger une fonction en python.

- Return

```
def nom_de_la_fonction():
    return valeur
```

#### Fonctions lambda

`f = lambda x: x * x`

#### Modules

`import math [as name_space]`

`math.sqrt(16)`

`name_space.sqrt(16)`

`from math import sqrt [as racine]`

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

`from mon_module import *`

Le nom du module ne doit pas commencer par un chiffre et ne doit pas contenir de '-'

Tests directement dans le module :

`if __name__ == "__main__":`

Permet de tester si le fichier appelé est le fichier exécuté.

- Module : permet de regrouper des fonctions
- Package : permet de regrouper des modules

Packages = répertoires

importer un package : `import nom_bibliotheque`
accéder à un sous package : `import nom_bibliotheque.sous_package`

fichier d'initialisation d'un package : `__init.py__`

### Les exceptions

Forme minimale :

```
try:
    # instruction
except:
    # catch
```

Forme complète :

```
try:
    # instruction
except typeError:
    # catch typeError
```

```
try:
    # instruction
except typeError as exceptionRetournee:
    # catch typeError (exceptionRetournee)
```

```
try:
    # instruction
except:
    # catch
else:
    # instruction si pas d'erreur
```

```
try:
    # instruction
except:
    # catch
finally:
    # instruction executée si erreur ou non
```

Le mot clé `pass` :

```
try:
    # instruction
except:
    pass # ne rien faire en cas d'exception
```

- Assertions

`assert test`

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

`chaine.lower()` : passe en minuscule chaine

`objet.methode()``

`chaine = str()` <=> `chaine = ""`

Formatage de chaines :

```
nom = "toto"
print("Hello {0}".format(nom))
```

Formatage avec noms de variables :

```
adresse = """
{no_rue}, {nom_rue}
{code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)
```

Concaténation avec + :

`chaine1 + chaine2`

Accéder aux caractères d'une chaine :

`chaine[i]`

On peut accéder aux caractères en partant de la fin (`chaine[-1]`)

Longueur d'une chaine : `len(chaine)`

Sélection de chaine : `chaine[0:2]`

### Listes et tuples (1/2)

#### Listes

Les listes sont des séquences comme les chaines de caractères qui peuvent contenir n'importe quel type d'objet au lieu de contenir des caractères.

Créer une liste vide :

```
ma_liste = list()
ma_liste = []
```

Créer une liste non vide : `ma_liste = [1,2,3,4,5]`

Accéder à un élément de la liste : `ma_liste[i]`

Ajouter un élément à la liste : `ma_liste.append(var)`

Concaténation de liste : `ma_liste1 + ma_liste2`

Suppression d'élément de liste :

```
del var / del ma_liste[i]
ma_liste.remove(var)
```

Parcours de liste :

```
i = 0
while i < len(ma_liste):
	# instruction
```

```
for element in ma_liste:
	# instruction
```

```
for i, element in enumerate(ma_liste):
	# instruction
```

```
for elt in enumerate(ma_liste):
	# elt est un tuple (indice, val)
```

#### tuples

Les tuples sont des listes immutables

Créer un tuple vide : `t = ()`

Créer un tuple non vide : `t = (1,)` / `t = 1,` / `t = (1,2,5)`

Les tuples peuvent être utilisés dans des fonctions pour retourner plusieurs valeurs.

### Listes et tuples (2/2)

#### Listes et chaines

Des chaines aux listes : `chaine.split(" ")`

Des listes aux chaines : `" ".join(tab)`

Fonction avec une liste de paramètres variable : `def fonc(*params)`

Transformer une liste en paramètres de fonctions :
```
tab = [1,3]
print(*tab)
```

#### Compréhensions de liste

- Permettent de modifier / filter une liste

```
>>> liste=[0,1,2,3,4]
>>> [nb * nb for nb in liste]
[0, 1, 4, 9, 16]
```

```
>>> [nb * nb for nb in liste if nb%2 == 0]
[0, 4, 16]
```

```
>>> toto=[
...     ("fraises", 7),
...     ("carotte",25)
... ]
```

```
>>> tata=[(qtt,nom) for nom,qtt in toto]
>>> sorted(tata)
[(7, 'fraises'), (25, 'carotte')]
```

La syntaxe pour effectuer un filtrage est la suivante : `nouvelle_squence = [element for element in ancienne_squence if condition].`

### Dictionnaires

#### Dict

Créer un dictionnaire vide :
```
d = dict()
d = {}
```

Créer un dictionnaire rempli :
`d = {cle1:val1,cleN:valN}xxx`

Ajouter des éléments :
`d[cle] = val`

Accéder à un élément :
`d[cle]`

ex avec cle tuple :
`d[a,1] = val`

Supprimer un élément :
```
del d[cle]
d.pop(cle)
```

On peut mettre des fonctions dans un dictionnaire :
```
d[cleFonc] = f
d[cleFonc]() equivalent à f()
```

Parcours des clés :

`for c in d.keys()`

Parcours des valeurs :

`for v in d.values()`

Parcours des clés et valeurs :

`for c,v in d.items()`

Test d'une valeur :

`if val in d.values()`

Fonction avec une liste de paramètres nommés variable : `def fonc(**params)`

Transformer une liste en paramètres de fonctions :
```
map = {cle:val,cleN:valN}
fonc(**tab)
```

#### Set

Créer un set :
```
s = set()
s = {val1,valN}
```

Ajouter un élément :
`s.add(val)`

### Fichiers

```
import os

os.chdir("/dir")
os.getcwd() : retourne le répertoire actuel
```

Ouvrir un fichier : `fic = open(path_file, mode)`
mode : `r` (read) ; `w` (write) ; `a` (append) ; `b` (binary)

Fermer un fichier : `fic.close()`

Ecrire du texte : `fic.write(text)`

Ouvrir un fichier sans avoir à gérer la fermeture en cas d'erreur :
```
with open(path_file, mode) as fic:
	# instructions
```

`with` permet de créer un context manager

Enregistrer un objet dans un fichier avec pickle :

```
import pickle
>>> with open('donnees', 'wb') as fichier:
...     mon_pickler = pickle.Pickler(fichier)
...     # enregistrement ...
```

`pickler.dump(obj)`

Lire un objet :

```
mon_unpickler = pickle.Unpickler(fichier)
obj = mon_unpickler.load()
```

### Portée des variables et références

- Portée dans l'espace local d'une fonction puis dans espace local appelant
- l'espace local d'une fonction n'existe que le temps d'exécution de la fonction

En python tout est objet. Lors de l'appel à une fonction, c'est l'objet qui est passé et non les valeurs. L'objet peut donc être modifié

Une variable est un nom identifiant pointant vers une référence d'un objet

ex: 
```
liste1 = [1,2,3]
liste2 = liste1
```

`liste1` et `liste2` pointent vers le même objet. Une modification sur l'un des objets entraine la modification de l'autre.

Pour faire une copie de l'objet il faut passer par le constructeur : `liste2 = list(liste1)`

Pour comparer le contenu : `==` (ex : `liste1 == liste2` si les deux listes contiennent les mêmes valeurs)
Pour comparer deux références : `is` (ex : `liste1 is liste2` si les deux variables référencent le même objet)

Pour qu'une fonction puisse modifier le contenu d'une variable contenue hors de la fonction il suffit de déclarer la variable globale :

```
i = 1
def fonc():
    global i
    # Instructions modification de i
```

## POO côté développeur

### Première approche des classes

Créer une classe avec un constructeur vide :

```
class NomClasse:
    def __init__(self):
        self.attr1 = val1
```

Le constructeur peut contenir des valeurs d'attributs (mais commence toujours par self)

```
def __init__(self, maVal):
    self.attr1 = maVal
```

Attributs de classe (equivalent static java) :

```
class NomClasse:
    obj_crees = 0

    def __init__(self):
        NomClasse.obj_crees +=1
```

Définir une méthode d'instance :

```
def methode(self, param):
    self.attr1 = param
```

Définir une méthode statique : on ne passe pas `self` en premier paramètre mais `cls`

`def methodeStatique(cls):`

Autre possibilité de methode appelée statiquement :

```
def uneMethode():
    # Instructions independante de l'instance

methodeStatique = staticmethod(uneMethode)
```

Introspection :

`dir(uneInstance)` : Affiche les attributs et méthodes de l'objet passé en paramètre
attribut spécial `__dict__` : `obj.__dict__` affiche les attributs/valeurs de l'objet

### Les propriétés

Les attributs sont toujours public en python.

Les propriétés sont un moyen transparent de manipuler les attributs :

```
class MaClasse:
    def __init(self)__:
        self._attr = "val"

    def _get_attr(self):
        # methode appelée lorsqu'on accède en lecture à l'attribut

    def _set_attr(self, val):
        # methode appelée lorsqu'on accède en écriture à l'attribut

    # On indique à python que notre attribut attr pointe vers une propriété
    attr = property(_get_attr,_set_attr)
```

Lorsqu'on appelle maclasse.attr : python passe par les getter et setter définis dans la propriété.

### Les méthodes spéciales

Les méthodes spéciales sont des méthodes d'instances.

#### Edition et accès aux attributs

- Méthodes d'éditions :
    - `__init__` : constructeur
    - `__del__` : destructeur
- Méthode de représentations :
    - `__str__` : équivalent de tostring
    - `__repr__` : comme __str__ si non implémentée. Méthode appelée implicitement avec la fonction repr(obj)
- Méthodes d'accès aux attributs :
    - `__getattr__` : appelée lorsqu'on essaie d'accéder à un attribut qui n'est pas défini
    - `__setattr__` : appelée lorsqu'on donne une valeur à un attribut
    - `__delattr__` : appelée lorsqu'on fait un del sur un attribut

#### Méthodes de conteneur

- Méthodes d'accès aux éléments
    - `__getitem__` : définit ce que l'on renvoie lorsqu'on fait objet[index]
    - `__setitem__` : définit ce que l'on renvoie lorsqu'on fait objet[index] = valeur
    - `__delitem__` : définit ce que l'on renvoie lorsqu'on fait del objet[index]
- Méthode derrière "in" :
    - `__contains__` : appelée lorsqu'on fait "elt in monObjet"
- Taille d'un conteneur :
    - `__len__` : appelée lorsqu'on fait len(objet)

#### Méthodes mathématiques

Elles permettent de définir les opérations à effectuer sur un objet lorsqu'on utilise les opérateurs mathématiques + - *...

- `__add__` : appelée lorsqu'on fait objet + objet
- `__sub__` : appelée lorsqu'on fait objet - objet
- `__mul__` : appelée lorsqu'on fait objet * objet
- `__truediv__` : appelée lorsqu'on fait objet / objet
- `__floordiv__` : appelée lorsqu'on fait objet // objet
- `__mod__` : appelée lorsqu'on fait objet % objet
- `__pow__` : appelée lorsqu'on fait objet ** objet
...

Attention au sens lorsqu'on effectue une opération sur 2 objets différents : c'est la méthode add du premier objet qui est utilisée. On peut faire marcher l'opération dans le sens inverse en préfixant la méthode par r :

- `__radd__`
- `__rsub__`
....

Les opérateurs += et -= peuvent être surchargés en préfixant par i :

- `__iadd__`
- `__isub__`

#### Méthodes de comparaison

Elles permettent de définir les opérations à effectuer sur un objet lorsqu'on utilise les opérateurs == <= >= ...

- `__eq__` = appelée lorsqu'on fait objet == objet
- `__ne__` = appelée lorsqu'on fait objet != objet
- `__gt__` = appelée lorsqu'on fait objet > objet
- `__ge__` = appelée lorsqu'on fait objet >= objet
- `__lt__` = appelée lorsqu'on fait objet < objet
- `__le__` = appelée lorsqu'on fait objet <= objet

Ce sont également ces méthodes qui sont appelées lorsqu'on trie une liste d'objets.

#### Méthodes utiles à pickle

Permettent de contrôler l'état d'un objet lors de la sérialisation / désérialisation :

- `__getstate__`
- `__setstate__`

### Parenthèse sur le tri

2 méthodes pour trier une liste :

- `maListe.sort()` : Ordonne les éléments de maListe
- `sorted(maListe)` : Fonction builtin qui renvoie une liste triée. MaListe n'est pas modifiée

On peut préciser la clé de tri en passant le paramètre optionnel key aux méthodes sort et sorted. Elle se définit comme une fonction :

ex :
`sorted(tab, key=lambda colonnes: colonnes[2])` : permet de trier sur la 3eme colonne du tableau

Pour trier un objet il faut soit :

- définir la fontion `__lt__` dans la classe de l'objet à trier
- passer par l'argument `key` pour dire à python comment trier nos objets

Pour trier dans l'ordre inverse on utilise le paramètre `reverse=True` dans les fonctions sort ou sorted

Pour des raisons de performance il est préférable d'utiliser le module operator plutôt que les fonctions lambda lors des tris :

ex :
```
from operator import itemgetter
sorted(tab, key=itemgetter(2))
```

Pour trier sur les attributs d'un objet on utilise `attrgetter`

Pour trier selon plusieurs critères on peut passer plusieurs arguments à `attrgetter`

Le tri en Python est « stable », c'est-à-dire que l'ordre de deux éléments dans la liste n'est pas modifié s'ils sont égaux. Cette propriété permet le chaînage de tri.

### L'héritage

#### Héritage simple

```
class A:
    pass

class B(A):
    pass
```

la classe B hérite de A

Dans le constructeur B si on veut appeler le constructeur A il faut le faire explicitement :
`A.__init__(self)`

Deux méthodes permettent de connaitre les instances :
- `issubclass` : Teste si une classe est une sous-classe d'une autre
- `isinstance` : permet de savoir si un objet est issu d'une classe ou de ses classes filles

#### Héritage multiple

```
class A:
    pass

class B:
    pass

class C(A,B):
    pass
```

La recherche de méthode a appeler suit l'ordre de définition : C > A > B

Créer une Exception personnalisée :

Doit hériter de :
- `BaseException`
- ou `Exception` (hérite elle même de BaseException)

Doit redéfinir le constructeur et `__str__`

### Derrière la boucle for

#### Les itérateurs

Les itérateurs interviennent lors des parcours de liste :

```
ma_liste = [1, 2, 3]
for i in ma_liste
```

Python utilise l'itérateur de `ma_liste`. L'itérateur est créé dans la méthode spéciale `__iter__` (la méthode renvoie un itérateur permettant de parcourir la liste).

A chaque tour de boucle python appelle la méthode `__next__` de l'itérateur qui doit renvoyer l'élément suivant du parcours ou lever l'exception `StopIteration` si le parcours est fini.

Création d'un itérateur :

```
class RevStr(str):
     def __iter__(self):
             return ItRevStr(self)

class ItRevStr:
     def __init__(self, chaine_a_parcourir):
             self.chaine_a_parcourir = chaine_a_parcourir
             self.position = len(chaine_a_parcourir)
     def __next__(self):
             if self.position == 0:
                     raise StopIteration
             self.position -= 1
             return self.chaine_a_parcourir[self.position]
```

Utilisation : 

```
>>> test = RevStr("Bonjour")
>>> test
'Bonjour'
>>> for lettre in test:
...     print(lettre)
...
r
u
o
j
n
o
B
```


