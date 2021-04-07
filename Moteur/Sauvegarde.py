class Moteur:    
    def sauvegarde(self,echiquier_a_sauvegarder):

        sauvegarde_tour = echiquier_a_sauvegarder[-1]
        sauvegarde_tour = str(sauvegarde_tour)
        echiquier_a_sauvegarder = str(echiquier_a_sauvegarder)
        fichier=open('Moteur/logs/sauvegarde_echec.txt','a+')
        fichier.write('Tour ')
        fichier.write(sauvegarde_tour)
        fichier.write(' : ')
        fichier.write(echiquier_a_sauvegarder)
        fichier.write( '\n' )
        fichier.close
        print("Sauvegarde du tour effectué")

        # cette fonction sauvegarde l'échiquier.