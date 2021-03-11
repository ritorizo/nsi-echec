# Cahier des charges du jeu d'echec

## Palier 1 : Interface Graphique et JcJ fonctionel

- Implémenter le Joueur contre Joueur sur la même machine.
- Affichage des pion.
- Controle des mouvements des pions avec le clavier (en indiquant les coordonés A et B).
- Faire en sorte que le jeu refuse les coups imposibles. 
- Le jeu signale quand un joueur gagne, qu'il y a égalité ou pat.

## Palier 2 : Implémentation d'une IA basique

- Au lancement d'un partie je jouer peut choisir entre une partie contre une IA ou un autre Joueur.
- L'IA utilise l'euristique a un niveau pour choirsir ces coups.

## Palier 3 : Sauvegarde 

- Evolution drawinienne des IA (avec des tournois).
- Bibliotéque d'ouverture.
- Implémentation d'un systéme de sauvgarde.
- Enregistrement et replay de la partie.
- Retour ariére.

## Palier 4

## Palier secret

- le robot joue aléatoirement

# Architechrure Logicielle

struct piece { char couleur ; char type }

list echiquier[8][8]

class Moteur
