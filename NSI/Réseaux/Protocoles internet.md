# Définition
![[Réseaux#Définitions]]

> [!note]
> Pour l'adresse IP : 172.168.0.0/16, signifie que les 16 bits de poids fort sont à 1 dans le masque de sous-réseau ; c'est comme si on écrivait 172.168.0.0 avec un masque de sous-réseau : 255.255.0.0 (11111111.11111111.00000000.00000000 en binaire).
> - Autre exemple : 192.168.7.2/24 = 192.168.7.2 avec masque de sous-réseau : 255.255.255.0.
# Protocoles
Les réseaux se comportent un peu comme des graphes, chaque routeur et switch est sommet et les liaisons des arrêtes. De ce fait, les algorithmes des [[Graph]], s'applique sur les réseaux, notamment la recherche du plus court chemin.
## Protocole RIP
![[Protocole RIP]]

# Protocole OSPF
![[Protocole OSPF]]
