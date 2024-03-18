# Définitions
- Adresse IP : Une adresse IP est un **numéro unique** qui identifie un appareil connecté à un réseau. C'est comme une adresse postale pour les ordinateurs. ex : *172.168.5.2*
- Adresse MAC : Identifiant unique attribué a chaque carte réseau, (un peu comme le numéros de série pour la carte réseau)
- Réseaux locaux : Les réseaux locaux (LAN) sont des réseaux informatiques utilisés dans des **endroits proches** les uns des autres, comme une *maison* ou un *bureau*, pour que les appareils puissent se connecter et communiquer entre eux.
- Switch : Un switch est un appareil qui **connecte plusieurs appareils dans un réseau local**. Il dirige les données uniquement vers l'appareil destinataire, ce qui rend les communications plus efficaces.
- Routeur  :Un routeur est un appareil qui **dirige le trafic réseau entre différents réseaux**. Il s'assure que les données parviennent de l'expéditeur au destinataire correctement.
- Masque de sous-réseau : Le masque de sous-réseau est une série de chiffres **utilisée pour diviser un réseau en sous-réseaux plus petits**. Cela permet d'organiser le trafic et de limiter la visibilité des appareils dans le réseau. ex: *255.255.255.0* 
  **Attention le masque peut prendre d'autres formes ex :** *255.240.00*
- Paquet : Un paquet est une **petite quantité de données envoyée sur un réseau informatique**. C'est comme un petit colis qui transporte des informations d'un endroit à un autre sur Internet. Chaque paquet contient les données à envoyer, ainsi que des instructions sur la manière de les livrer à leur destination.

> [!note]
> Pour l'adresse IP : 172.168.0.0/16, signifie que les 16 bits de poids fort sont à 1 dans le masque de sous-réseau ; c'est comme si on écrivait 172.168.0.0 avec un masque de sous-réseau : 255.255.0.0 (11111111.11111111.00000000.00000000 en binaire).
> - Autre exemple : 192.168.7.2/24 = 192.168.7.2 avec masque de sous-réseau : 255.255.255.0.
# Protocoles
# Protocole RIP
[[Exemple de routage RIP.canvas|Exemple de routage RIP]]
![[Exemple de routage RIP.png]]
