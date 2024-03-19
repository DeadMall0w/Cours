![[Réseaux#Définitions]]

# Utilisation 
Prenons l'exemple d'un appareil placé connecté a internet, avec l'adresse IP : 192.168.1.5, et un masque de sous réseau 255.255.255.0

Ce masque sert à avoir l'adresse du réseau.
Pour récupérer l'adresse du réseaux, il faut d'abord convertir l'adresse IP et le masque en binaire [[Conversion Binaire]].
192.168.1.5        : 11000000.10101000.00000001.00000101
255.255.255.0  : 11111111.11111111.11111111.00000000
Il suffit ensuite d'appliquer la [[Porte ET]] a ces 2 nombres

11000000.10101000.00000001.00000101
11111111.11111111.11111111.00000000
. = 11000000.10101000.00000001.00000000
On reconvertit en nombre entier
Adresse réseau : 192.168.1.0

## Trouver le nombre d'appareil connecté
On peut trouver le nombre d'appareil maximum qu'on peut connecté un réseau en meme temps, a l'aide du masque de sous réseau

Il faut compter combien de bit sont a 0.

> [!note]
> Les adresses ip 255.255.255.255 et 255.255.255.0 sont reservé, alors il faut enlever 2 au résultat.
> 

Ex : 255.255.255.0
il y a 8 bit a 0, donc $2⁸-2$, soit $255-2 = 253$ réseaux possible.

Ex : 255.255.0.0
il y a 16 bit a 0, donc $2^{16}-2$ réseaux possible.