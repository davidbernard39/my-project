def trier(li):
    li=[(nb, fruit) for fruit, nb in li]
    li.sort(reverse=True)
    return li

def trier2(li):
    return sorted([(nb, fruit) for fruit, nb in li], reverse=True)

inventaire = [
 ("pommes", 22),
 ("melons", 4),
 ("poires", 18),
 ("fraises", 76),
 ("prunes", 51),
]

print(inventaire)
inventaire2=trier(inventaire)
print(inventaire2)
inventaire3=trier2(inventaire)
print(inventaire3)
