
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
- \[[[TB][][KN][][][][][]] [[][][][][QB][][][]] [[][][][][][][][]] [[][][][][][][][]] [[][][][][][KB][][]] [[][][][][][][][]] [[PB][][][][][][][]] [[][][][][][][][]] 24\]


##Les cordonnées d'une pièce

les cordonnées d'une pièce sont définie par un tuple (contenant une lettre majuscule(A  B  C  D  E  F  G  H)et un chifre(1  2  3  4  5  6  7  8))

ex:
(B5)

##Les mouvements de pièces

le mouvement d'une piece est définie par un tuple(contenant 2 tuple( le premier contenant les cordonées de départ de la pièce et le second tuple les cordonnées d'arrivée))

ex:
((A5)(B6))

### class Moteur

	description : cette class gére la partie.

	```echiquier jeu_actuel```
		L'échiquier qui représente le status de la partie.

	```méthdoe getEchiqier() : echiqier```
		renvois l'échiquier.

	```methode lancement(string) : rien``` 
		Prend une chaine composé de deux charactéres, le premier charactére représente l'agent qui va jouer les blanc et le deuxiéme celui qui va jouer les noir.

		Pour l'instant les agents suivant sont prévu :
			"J" : Un joueur humain qui utilise la machine sur laquelle le jeu tourne.
			"R" : Une intelligente artificielle basique.

	```methode coupValide(mouvement) : boolean```
		Renvois True si le mouvement présenté est possible, sinon renvois False.

	```methode boucleDeJeu(echiquier) : rien```
		Demande a l'agent dont c'est le tour son action par le biais de la méthode jouerTour(), applique les changement en éditant l'échiqier jeu_actuel et actualise l'interface graphique.


## class Interface
	
	description : cette class gére l'interface utilisateur.

	
	```demanderCoup() : mouvement```
		Demande a l'utilisateur de déplacer une piéce et renvois le mouvement choisi.
	
	```deplacePiece(mouvement) : rien``` 
		Déplace une piéce sur l'échiquer.

	```changeEchiqier(echiqier)```
		Affiche l'échiqier mis en parapétre.

## class Agent

	description : La classe agent est une classe qui sert a faire se que sa seule méthode fait : demander a un joueur se qu'il veut faire. Elle a été faite dans le but te pouvoir interagir avec nimporte quel type de joueur (Joueur local, IA, joueur distant...) de la même maniére.

	```jouerTour() : mouvement```
		Demande a l'agent quelle piéce il veut déplacer
