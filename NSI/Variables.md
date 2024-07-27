Python est un langage de programmation dynamique qui offre une grande variété de types de variables. Comprendre ces types est essentiel pour écrire des programmes efficaces et robustes. Ce cours couvre les types de base, les collections, et les types avancés en Python.

## Types de Base

### 1. Entiers (int)

Les entiers sont des nombres sans partie décimale.

**Exemple :**

```python
a = 10
b = -5
```

### 2. Flottants (float)

Les flottants sont des nombres à virgule flottante, utilisés pour les valeurs avec des parties décimales.

**Exemple :**

```python
x = 3.14
y = -0.001
```

### 3. Chaînes de caractères (str)

Les chaînes de caractères sont des séquences de caractères entourées de guillemets simples (' ') ou doubles (" ").

**Exemple :**

```python
nom = "Alice"
phrase = 'Bonjour, le monde!'
```

### 4. Booléens (bool)

Les booléens sont des variables qui ne peuvent prendre que deux valeurs : `True` ou `False`.

**Exemple :**

```python
vrai = True
faux = False
```

## Types de Collections

### 1. Listes (list)

Les listes sont des collections ordonnées et modifiables d'éléments.

**Exemple :**

```python
fruits = ["pomme", "banane", "cerise"]
nombres = [1, 2, 3, 4, 5]
```

### 2. Tuples (tuple)

Les tuples sont des collections ordonnées mais immuables d'éléments.

**Exemple :**

```python
coordonnées = (10.0, 20.0)
couleurs = ("rouge", "vert", "bleu")
```

### 3. Ensembles (set)

Les ensembles sont des collections non ordonnées d'éléments uniques.

**Exemple :**

```python
animaux = {"chat", "chien", "lapin"}
nombres_uniques = {1, 2, 3, 4, 5}
```

### 4. Dictionnaires (dict)

Les dictionnaires sont des collections non ordonnées de paires clé-valeur.

**Exemple :**

```python
étudiant = {"nom": "Alice", "âge": 21, "cours": "maths"}
prix_fruits = {"pomme": 0.5, "banane": 0.3, "cerise": 1.0}
```

## Types Avancés

### 1. NoneType

Le type `None` représente l'absence de valeur ou une valeur nulle.

**Exemple :**

```python
rien = None
```

### 2. Types de collections immuables

Les types de collections immuables incluent les **frozensets**, qui sont comme des ensembles mais immuables.

**Exemple :**

```python
frozen_set = frozenset([1, 2, 3, 4, 5])
```

## Utilisation et Manipulation des Variables

### Assignation Multiple

Python permet d'assigner plusieurs variables en une seule ligne.

**Exemple :**

```python
a, b, c = 1, 2, 3
```

### Conversion de Types

Python permet de convertir les types de variables à l'aide des fonctions intégrées comme `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, et `dict()`.

**Exemple :**

```python
num_str = "123"
num_int = int(num_str)  # Convertir chaîne en entier
num_float = float(num_int)  # Convertir entier en flottant

liste = [1, 2, 3]
tuple_liste = tuple(liste)  # Convertir liste en tuple
```

## Conclusion

Comprendre les types de variables en Python est crucial pour écrire des programmes efficaces et clairs. Les types de base, les collections et les types avancés offrent une grande flexibilité pour stocker et manipuler les données. Les notions de mutabilité et d'immuabilité sont également importantes pour comprendre comment les données peuvent être modifiées au sein des programmes.
