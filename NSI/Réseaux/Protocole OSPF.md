# Définition
OSPF = Open Shortest Path First
Le protocole OSPF est un protocole de routage utilisé **dans les réseaux informatiques** pour permettre aux routeurs de communiquer entre eux et de partager des informations sur les **chemins les plus efficaces** pour atteindre les réseaux de destination.
Contrairement au [[Protocole RIP]], ce protocole utilise les bandes passantes pour trouver les chemins les plus courts. Il vise a **prioriser les connections où la bande passante est la plus forte**, permettant des chemins plus rapide qu'avec le [[Protocole RIP]].

# Fonctionnement
Un coût est associé a chaque connection entre routeur, avec la formule suivante : $coût = \dfrac{10^{8}}{debit}$.
Le débit est en b/s.

> [!danger] Attention
> Ne pas oublier de convertir les unités [[Conversion des Unités de Poids Informatique]].
> De plus, la formule de coût peux varié d'un exercice à l'autre, si elle change cela sera indiqué

A l'aide de l'[[Algorithme de Dijkstra]] on peut trouver le plus court chemin

# Utilisation

![[Exemple de routage OSPF.png]]
### Tables des coûts 

| Vitesse    | Coût                         |
| ---------- | ---------------------------- |
| 1Mbits/s   | $\dfrac{10^8}{10^6} = 100$   |
| 10Mbits/s  | $\dfrac{10^8}{10^6} = 10$    |
| 100Mbits/s | $\dfrac{10^8}{10^8} = 1$     |
| 1Gbits/s   | $\dfrac{10^8}{10^9} = 0.1$   |
| 10Gbits/s  | $\dfrac{10^8}{10^{10}} = 0.01$ |
### Application
![[Exemple de routage OSPF avec cout.png]]
Les coûts ont été rajoutés en rouge.
#### Exemple avec le routeur A
| Destination | Prochain routeur | Coût |
| ----------- | ---------------- | ---- |
| B           | B                | 1    |
| C           | B                | 1,1  |
| D           | F                | 11,2 |
| E           | F                | 1,1  |
| F           | F                | 0,1  |
| G           | F                | 1,2  |
... Pour les autres routeurs