# Définition
RIP = Routing information Protocol
Le protocole RIP est un protocole de routage utilisé **dans les réseaux informatiques** pour permettre aux routeurs de communiquer entre eux et de partager des informations sur les **chemins les plus efficaces** pour atteindre les réseaux de destination.
# Fonctionnement
Les routeurs qui utilisent RIP **envoient périodiquement** des mises à jour de routage à leurs voisins pour informer les autres routeurs des réseaux qu'ils peuvent atteindre et des coûts associés à ces routes. Chaque routeur utilise ces informations pour **construire une table de routage**, qui est utilisée pour prendre des décisions sur la manière de transférer les paquets de données.

Utilise comme métrique le **nombre de saut** pour trouver le meilleur chemin, ce qui permet une faciliter d'implémentation et d'utilisation. Cependant elle ne prend pas en compte la bande passante, alors, le chemin trouvé n'est pas forcément **le plus rapide**, mais celui comportant le moins de saut.
De plus, le protocole RIP est **limité à 15 sauts** (on traverse au maximum 15 routeurs pour atteindre sa destination), ce qui limite fortement la taille des réseaux.

# Utilisation
[[Exemple de routage RIP.canvas|Exemple de routage RIP]]
![[Exemple de routage RIP.png]]
On fait une recherche du plus court chemin, notamment avec l'[[Algorithme de Dijkstra]]
## Exemple avec le routeur A
| Destination | Prochain routeur | Coût (nb saut) |
| ----------- | ---------------- | -------------- |
| B           | B                | 1              |
| C           | C                | 1              |
| D           | C                | 2              |
| E           | F                | 2              |
| F           | F                | 1              |
| G           | F/C              | 3              |
... Pour les autres routeurs
