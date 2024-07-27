## Les Files

### Introduction

Les **files** sont des structures de données linéaires qui suivent le principe du **FIFO** (First In, First Out), ce qui signifie que le premier élément inséré est le premier à être retiré. Les files sont couramment utilisées dans les scénarios où les tâches doivent être traitées dans l'ordre d'arrivée.

### Propriétés et Opérations

- **Enfiler** : Ajout d'un élément à la fin de la file.
- **Défiler** : Retrait de l'élément en tête de la file.
- **Tête** : Accès à l'élément en tête sans le retirer.
- **Sommet** : Accès à l'élément en queue sans le retirer.
- **EstVide** : Vérification si la file est vide.
- **Taille** : Obtention du nombre d'éléments dans la file.

### Implémentation en Python

**Utilisation d'une liste :**

```python
class File:
    def __init__(self):
        self.file = []

    def enfiler(self, element):
        self.file.append(element)

    def defiler(self):
        if not self.est_vide():
            return self.file.pop(0)
        return None

    def est_vide(self):
        return len(self.file) == 0

    def tete(self):
        if not self.est_vide():
            return self.file[0]
        return None

    def sommet(self):
        if not self.est_vide():
            return self.file[-1]
        return None

    def taille(self):
        return len(self.file)
```

### Exemples d'utilisation

**Exemple 1 :**

```python
file = File()
file.enfiler(1)
file.enfiler(2)
file.enfiler(3)
print(file.defiler())  # Affiche 1
print(file.tete())     # Affiche 2
print(file.sommet())    # Affiche 3
print(file.taille())   # Affiche 2
```

### Applications des Files

- Gestion des tâches en attente (ex : impression de documents).
- Modélisation des files d'attente (ex : dans les magasins).
- Traversée des graphes en largeur (BFS).

## Les Piles

### Introduction

Les **piles** sont des structures de données linéaires qui suivent le principe du **LIFO** (Last In, First Out), ce qui signifie que le dernier élément inséré est le premier à être retiré. Les piles sont couramment utilisées dans les scénarios où le traitement doit suivre l'ordre inverse de l'arrivée.

### Propriétés et Opérations

- **Empiler** : Ajout d'un élément au sommet de la pile.
- **Dépiler** : Retrait de l'élément au sommet de la pile.
- **Sommet** : Accès à l'élément au sommet sans le retirer.
- **EstVide** : Vérification si la pile est vide.
- **Taille** : Obtention du nombre d'éléments dans la pile.

### Implémentation en Python

**Utilisation d'une liste :**

```python
class Pile:
    def __init__(self):
        self.pile = []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.pile.pop()
        return None

    def est_vide(self):
        return len(self.pile) == 0

    def sommet(self):
        if not self.est_vide():
            return self.pile[-1]
        return None

    def taille(self):
        return len(self.pile)
```

### Exemples d'utilisation

**Exemple 1 :**

```python
pile = Pile()
pile.empiler(1)
pile.empiler(2)
pile.empiler(3)
print(pile.depiler())  # Affiche 3
print(pile.sommet())   # Affiche 2
print(pile.taille())   # Affiche 2
```

### Applications des Piles

- Gestion des appels de fonctions (pile d'appels).
- Évaluation d'expressions arithmétiques (notation postfixée).
- Parcours des arbres en profondeur (DFS).
- Vérification de parenthèses équilibrées dans les expressions.

## Comparaison entre Files et Piles

| Caractéristique        | File                       | Pile                        |
| ---------------------- | -------------------------- | --------------------------- |
| Principe               | FIFO (First In, First Out) | LIFO (Last In, First Out)   |
| Opération d'ajout      | Enfiler (à la fin)         | Empiler (au sommet)         |
| Opération de retrait   | Défiler (en tête)          | Dépiler (au sommet)         |
| Accès aux éléments     | Tête, Sommet               | Sommet                      |
| Utilisations courantes | Files d'attente, BFS       | Pile d'appels, DFS, calculs |

## Conclusion

Les **files** et les **piles** sont des structures de données fondamentales en programmation. Les files sont utilisées pour des tâches où l'ordre d'arrivée doit être respecté, tandis que les piles sont utilisées pour des tâches où le dernier élément ajouté est le premier à être traité. La compréhension et l'utilisation appropriée de ces structures permettent d'écrire des programmes plus efficaces et mieux structurés.
