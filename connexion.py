#!/usr/bin/python3

import psycopg2
import fonctions

HOST = "tuxa.sme.utc"
USER = "nf18a063"
PASSWORD = "4xN6OyUtdyA8"
DATABASE = "dbnf18a063"

# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

MENU = """Menu :\n 
      1. Voir les informations d'un patient (espèce,nom,prenom)\n 
      2. Voir les informations d'un vétérinaire (nom,prenom,spécialité)\n 
      3. Quitter\n"""

choix = int(input(MENU))
while(choix != 3):
    if(choix == 1):
        id = int(input("Entrez l'id du vétérinaire pour lequel vous voulez consulter les informations"))
        fonctions.afficheVeterinaire(conn,id)
    if(choix == 2):
        id = int(input("Entrez l'id du patient pour lequel vous voulez consulter les informations"))
        fonctions.affichePatient(conn,id)
    choix = int(input(MENU))

# Commit (transactionnal mode is by default)
conn.commit()

# Close connection
conn.close()