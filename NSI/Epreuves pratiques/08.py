# Sujet 8 - 2022

# Exercice 1
def recherche(elt:int, tab:list)->int:
    """
    Renvoie l'indice de la première occurrence de elt dans tab

    Paramètre:
    elt - int : element a rechercher
    tab - list : Liste dans laquelle on recherche

    Retour:
    int : l'indice de la première occurrence de elt dans tab ou -1 si elt n'est pas dans tab
    Sans effet de bord
    """
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1

# Test
print("Exercice 1:")
print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))


# Exercice 2

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < tab[i] and i >= 0: 
        l[i+1] = l[i]
        l[i] = a
        i = i -1
    return l


# Test
print("Exercice 2:")
print(insere(3,[1,2,4,5]))
print(insere(10,[1,2,7,12,14,25]))
print(insere(1,[2,3,4]))
