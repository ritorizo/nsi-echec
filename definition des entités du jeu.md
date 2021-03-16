
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


##les cordonné d'une piece

les cordonné d'une piece sont définie par un tuple (ontenant une lettre majuscule(A  B  C  D  E  F  G  H)et un chifre(1  2  3  4  5  6  7  8))

ex:
(B5)

##LES MOUVEMENT DE PIECE

le mouvement d'une piece est définie par un tuple(contenant 2 tuple( le premier contenat les cordoné de dépar de la piece et le seguon les cordonné d'arriver))

ex:
((A5)(B6))
