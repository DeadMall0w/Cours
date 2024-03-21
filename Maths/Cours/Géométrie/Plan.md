# Introduction
A FAIRE

# Propriété du plan
- Les plans sont infinis dans toutes les directions.
- Deux plans sont parallèles s'ils ont des [[Vecteur normal du plan]] identiques.
- Deux plans sont perpendiculaires s'ils ont des [[Vecteur normal du plan]] perpendiculaires.
- L'intersection de deux plans est soit une droite, soit un plan, soit un point (si les plans sont identiques).

# Obtention d'un Plan
- A partir de 3 points non aligné 
- À partir d'un point et d'un [[Vecteur normal du plan]].
- À partir d'une [[Equation cartesienne de plan]] de la forme $Ax+By+Cz+D=0$.
# Utilisation
## Verifier si un point est dans un plan
![[Verifier si un point est sur un plan<embed>]]

## Position des plans entre eux
Soient 2 plans $P_{1}$ et $P_{2}$, de [[Vecteur normal du plan]] $\vec{n_{1}}$ et $\vec{n_{2}}$.
Ces 2 plans peuvent être :
- Parallèles, si  $\vec{n_{1}}$ et $\vec{n_{2}}$ sont [[Colinéaire]].
- Sécant si $\vec{n_{1}}$ et $\vec{n_{2}}$ **ne** sont **pas** [[Colinéaire]].
	- Sécant en une **droite** si $\vec{n_{1}}.\vec{n_{2}} \neq 0$.
	- Sont orthogonaux si $\vec{n_{1}}.\vec{n_{2}} = 0$

<button id="toggleButton">Afficher/Masquer</button>


## Position d'une droite et d'un plan
Soient un plan $P$ de [[Vecteur normal du plan]] $\vec{n}$ et une droite $d$ de [[Vecteur directeur]] $\vec{u}$.
Ces 2 objets peuvent être : 
- parallèle, si $\vec{n}$
	- Contenue
- Sécant en un point
- Perpendiculaire au plan, si 