# Cours sur le Système Binaire

Le **système binaire** est un système de numération de base 2, utilisé en informatique et en électronique. Il n'utilise que deux chiffres : 0 et 1. Voici un cours complet sur le système binaire, avec des explications et des exemples.

## Introduction au Système Binaire

En binaire, chaque chiffre est une puissance de 2. La position des chiffres détermine leur valeur, tout comme le système décimal (base 10) que nous utilisons couramment.

### Représentation Binaire

| Décimal | Binaire |
| ------- | ------- |
| 0       | 0       |
| 1       | 1       |
| 2       | 10      |
| 3       | 11      |
| 4       | 100     |
| 5       | 101     |
| 6       | 110     |
| 7       | 111     |
| 8       | 1000    |
| 9       | 1001    |
| 10      | 1010    |

## Conversion entre Binaire et Décimal

### Conversion de Binaire à Décimal

Pour convertir un nombre binaire en décimal, on multiplie chaque chiffre binaire par 2 élevé à la puissance de sa position (en partant de 0 à droite) et on additionne les résultats.

**Exemple :**

Convertir le binaire `1011` en décimal :

```
1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0
= 8 + 0 + 2 + 1
= 11
```

### Conversion de Décimal à Binaire

Pour convertir un nombre décimal en binaire, on divise le nombre par 2 et on note le reste. On continue à diviser le quotient par 2 jusqu'à ce que le quotient soit 0. Les restes, lus de bas en haut, forment le nombre binaire.

**Exemple :**

Convertir le décimal `13` en binaire :

```
13 / 2 = 6, reste 1
6 / 2 = 3, reste 0
3 / 2 = 1, reste 1
1 / 2 = 0, reste 1

Le binaire est 1101.
```

## Opérations en Binaire

### Addition

L'addition binaire suit les mêmes règles que l'addition décimale, mais avec une base de 2. Les règles de base sont :

- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0 et on retient 1)

**Exemple :**

```
  1011
+ 1101
------
 11000
```

### Soustraction

La soustraction binaire utilise les mêmes principes que la soustraction décimale, mais avec une base de 2. Les règles de base sont :

- 0 - 0 = 0
- 1 - 0 = 1
- 1 - 1 = 0
- 0 - 1 = 1 (et on emprunte 1 au chiffre suivant)

**Exemple :**

```
  1010
- 0011
------
  0111
```

### Multiplication

La multiplication binaire est similaire à la multiplication décimale mais plus simple, car elle n'utilise que 0 et 1. Les règles de base sont :

- 0 * 0 = 0
- 0 * 1 = 0
- 1 * 0 = 0
- 1 * 1 = 1

**Exemple :**

```
  101
*  11
------
  101
 101 
------
 1111
```

### Division

La division binaire est semblable à la division décimale, mais plus simple car elle n'utilise que 0 et 1.

**Exemple :**

```
 1011 ÷ 10

 1011
-1000
------
  0110
- 0100
------
   0010
-  0000
------
   0010
```

Le quotient est 101 et le reste est 1.

## Applications du Système Binaire

- **Informatique** : Les ordinateurs utilisent le binaire pour toutes leurs opérations internes car les circuits électroniques ont deux états : marche (1) et arrêt (0).
- **Réseaux** : Les adresses IP, les masques de sous-réseau et les adresses MAC sont souvent représentés en binaire.
- **Codage** : Le binaire est utilisé pour représenter des données et des instructions en code machine.

## Conclusion

Le **système binaire** est fondamental pour l'informatique et l'électronique. Comprendre comment convertir entre binaire et décimal, et comment effectuer des opérations arithmétiques en binaire, est essentiel pour travailler avec des systèmes numériques.
