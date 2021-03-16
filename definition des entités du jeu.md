
## Piéces d'échiquier:

Les pièces d'échiquier sont représentés par des chaines de deux caractères. Le premier charactére représente **le type de la pièce** et le deuxiéme **sa couleur**.

ex : une tour noire "TN"

|lettre|couleur|
|:----:|-------|
|N     |Noir   |
|B     |Blanc  |

|lettre | type    |
|:-----:|---------|
| K	| Roi     |
| Q	| Reine  |
| F	| Fou     |
| C	| Cavalier|
| T     | Tour    |
| P	| Pion    |

## Échiquier:
l'échiquier est définie par une liste (de 8 liste (de 8 liste (qui seront soit vide, soit contenant une string de 2 caractère(un pion))))et un int qui sera le numéro du tour   

ex :
- [[[TB][][KN][][][][][]] [[][][][][QB][][][]] [[][][][][][][][]] [[][][][][][][][]] [[][][][][][KB][][]] [[][][][][][][][]] [[PB][][][][][][][]] [[][][][][][][][]] 24]


##Les cordonnées d'une pièce

les cordonnées d'une pièce sont définie par un tuple (contenant une lettre majuscule(A  B  C  D  E  F  G  H)et un chifre(1  2  3  4  5  6  7  8))

ex:
(B5)

##Les mouvements de pièces

le mouvement d'une piece est définie par un tuple(contenant 2 tuple( le premier contenant les cordonées de départ de la pièce et le second tuple les cordonnées d'arrivée))

ex:
((A5)(B6))
