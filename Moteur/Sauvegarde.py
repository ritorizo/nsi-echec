def sauvegarde(echiquier):
    sauvegarde_tour = echiquier[-1]
    sauvegarde_tour = str(sauvegarde_tour)
    echiquier = str(echiquier)
    fichier=open('Moteur/logs/sauvegarde_echec.txt','a+')
    fichier.write('Tour ')
    fichier.write(sauvegarde_tour)
    fichier.write(' : ')
    fichier.write(echiquier)
    fichier.write( '\n' )
    fichier.close
    print("Sauvegarde du tour effectué")